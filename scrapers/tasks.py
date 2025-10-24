from celery_app import celery_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from config import settings
from generic_scraper import GenericCouponScraper
from javascript_scraper import JavaScriptCouponScraper
from affiliate_utils import generate_affiliate_url
import logging
import sys
import os

# Add parent directory to path to import models
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.models import Store, Coupon, ScrapeLog

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

@celery_app.task(name='tasks.scrape_store')
def scrape_store(store_id: int):
    """
    Scrape a single store for coupons
    """
    db = SessionLocal()
    start_time = datetime.utcnow()
    
    try:
        # Get store from database
        store = db.query(Store).filter(Store.id == store_id).first()
        
        if not store or not store.is_active:
            logger.warning(f"Store {store_id} not found or inactive")
            return
        
        logger.info(f"Starting scrape for {store.name}")
        
        # Convert SQLAlchemy model to dict
        store_dict = {
            'id': store.id,
            'name': store.name,
            'domain': store.domain,
            'region': store.region,
            'country': store.country,
            'affiliate_network': store.affiliate_network,
            'affiliate_id': store.affiliate_id,
            'merchant_id': store.merchant_id,
            'scraper_config': store.scraper_config or {}
        }
        
        # Determine scraper type
        scraper_type = store_dict['scraper_config'].get('type', 'generic')
        
        # Initialize appropriate scraper
        if scraper_type == 'javascript':
            scraper = JavaScriptCouponScraper(store_dict)
        else:
            scraper = GenericCouponScraper(store_dict)
        
        # Scrape coupons
        scraped_coupons = scraper.scrape()
        
        # Process and save coupons
        new_count = 0
        updated_count = 0
        
        for coupon_data in scraped_coupons:
            try:
                # Check if coupon exists
                existing = db.query(Coupon).filter(
                    Coupon.store_id == store_id,
                    Coupon.code == coupon_data['code']
                ).first()
                
                # Generate affiliate URL
                affiliate_url = generate_affiliate_url(store_dict, coupon_data)
                
                if existing:
                    # Update existing coupon
                    existing.title = coupon_data.get('title', existing.title)
                    existing.description = coupon_data.get('description', existing.description)
                    existing.expires_at = coupon_data.get('expires_at', existing.expires_at)
                    existing.discount_value = coupon_data.get('discount_value', existing.discount_value)
                    existing.discount_type = coupon_data.get('discount_type', existing.discount_type)
                    existing.affiliate_url = affiliate_url
                    existing.scraped_at = datetime.utcnow()
                    existing.is_active = True
                    updated_count += 1
                else:
                    # Create new coupon
                    new_coupon = Coupon(
                        store_id=store_id,
                        code=coupon_data['code'],
                        title=coupon_data.get('title', 'Discount Code'),
                        description=coupon_data.get('description'),
                        expires_at=coupon_data.get('expires_at'),
                        discount_value=coupon_data.get('discount_value'),
                        discount_type=coupon_data.get('discount_type', 'percentage'),
                        affiliate_url=affiliate_url,
                        source_url=coupon_data.get('source_url'),
                        scraped_at=datetime.utcnow()
                    )
                    db.add(new_coupon)
                    new_count += 1
            
            except Exception as e:
                logger.error(f"Error processing coupon {coupon_data.get('code')}: {e}")
                continue
        
        # Update store last_scraped_at
        store.last_scraped_at = datetime.utcnow()
        
        # Create scrape log
        duration = (datetime.utcnow() - start_time).seconds
        scrape_log = ScrapeLog(
            store_id=store_id,
            status='success',
            coupons_found=len(scraped_coupons),
            coupons_new=new_count,
            coupons_updated=updated_count,
            duration_seconds=duration
        )
        db.add(scrape_log)
        
        db.commit()
        
        logger.info(f"Scraped {store.name}: {new_count} new, {updated_count} updated, {len(scraped_coupons)} total")
        
        return {
            'store': store.name,
            'new': new_count,
            'updated': updated_count,
            'total': len(scraped_coupons)
        }
    
    except Exception as e:
        # Log failure
        logger.error(f"Failed to scrape store {store_id}: {e}")
        
        scrape_log = ScrapeLog(
            store_id=store_id,
            status='failed',
            error_message=str(e),
            duration_seconds=(datetime.utcnow() - start_time).seconds
        )
        db.add(scrape_log)
        db.commit()
        
        raise
    
    finally:
        db.close()

@celery_app.task(name='tasks.scrape_all_stores')
def scrape_all_stores():
    """
    Queue scraping tasks for all active stores
    """
    db = SessionLocal()
    
    try:
        # Get all active stores
        stores = db.query(Store).filter(Store.is_active == True).all()
        
        logger.info(f"Queuing scraping for {len(stores)} stores")
        
        queued = 0
        for store in stores:
            # Check if enough time has passed since last scrape
            if store.last_scraped_at:
                time_since_scrape = (datetime.utcnow() - store.last_scraped_at).total_seconds() / 60
                if time_since_scrape < store.scrape_frequency:
                    logger.debug(f"Skipping {store.name} - scraped {time_since_scrape:.1f} min ago")
                    continue
            
            # Queue scraping task
            scrape_store.delay(store.id)
            queued += 1
        
        logger.info(f"Queued {queued} stores for scraping")
        return {'queued': queued, 'total': len(stores)}
    
    finally:
        db.close()

@celery_app.task(name='tasks.cleanup_expired_coupons')
def cleanup_expired_coupons():
    """
    Deactivate expired coupons
    """
    db = SessionLocal()
    
    try:
        # Deactivate coupons past expiry date
        expired_count = db.query(Coupon).filter(
            Coupon.expires_at < datetime.utcnow(),
            Coupon.is_active == True
        ).update({'is_active': False})
        
        db.commit()
        
        logger.info(f"Deactivated {expired_count} expired coupons")
        return {'deactivated': expired_count}
    
    finally:
        db.close()

@celery_app.task(name='tasks.reset_daily_limits')
def reset_daily_limits():
    """
    Reset daily coupon counts for all users
    """
    db = SessionLocal()
    
    try:
        from backend.models import User
        
        # Reset daily_coupon_count for all users
        db.query(User).update({
            'daily_coupon_count': 0,
            'last_coupon_reset': datetime.utcnow()
        })
        
        db.commit()
        
        logger.info("Reset daily limits for all users")
        return {'status': 'success'}
    
    finally:
        db.close()
