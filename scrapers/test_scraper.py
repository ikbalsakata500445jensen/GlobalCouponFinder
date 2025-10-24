#!/usr/bin/env python3
"""
Test script for GlobalCouponFinder Scraping Service
Tests scrapers locally before deploying to Railway
"""
import os
import sys
import logging
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_imports():
    """Test that all modules can be imported"""
    try:
        from config import settings
        from base_scraper import BaseScraper
        from generic_scraper import GenericCouponScraper
        from javascript_scraper import JavaScriptCouponScraper
        from affiliate_utils import generate_affiliate_url
        from celery_app import celery_app
        from tasks import scrape_store, scrape_all_stores
        
        logger.info("✅ All imports successful")
        return True
    except Exception as e:
        logger.error(f"❌ Import error: {e}")
        return False

def test_generic_scraper():
    """Test generic scraper with a mock store"""
    try:
        from generic_scraper import GenericCouponScraper
        
        # Mock store data
        mock_store = {
            'name': 'Test Store',
            'domain': 'example.com',
            'scraper_config': {
                'type': 'generic',
                'coupon_list_url': 'https://httpbin.org/html',
                'selectors': {
                    'coupon_container': 'h1',
                    'code': 'h1',
                    'title': 'h1'
                }
            }
        }
        
        scraper = GenericCouponScraper(mock_store)
        logger.info("✅ Generic scraper created successfully")
        return True
    except Exception as e:
        logger.error(f"❌ Generic scraper error: {e}")
        return False

def test_affiliate_utils():
    """Test affiliate URL generation"""
    try:
        from affiliate_utils import generate_affiliate_url
        
        # Test different affiliate networks
        test_stores = [
            {'domain': 'amazon.com', 'affiliate_network': 'amazon', 'region': 'america'},
            {'domain': 'walmart.com', 'affiliate_network': 'shareasale', 'merchant_id': '123'},
            {'domain': 'target.com', 'affiliate_network': 'cj', 'merchant_id': '456'},
        ]
        
        for store in test_stores:
            url = generate_affiliate_url(store)
            logger.info(f"Generated URL for {store['domain']}: {url}")
        
        logger.info("✅ Affiliate URL generation working")
        return True
    except Exception as e:
        logger.error(f"❌ Affiliate utils error: {e}")
        return False

def test_celery_config():
    """Test Celery configuration"""
    try:
        from celery_app import celery_app
        
        # Check if Celery app is configured
        if celery_app.conf.broker_url:
            logger.info("✅ Celery broker configured")
        else:
            logger.warning("⚠️ Celery broker not configured")
        
        if celery_app.conf.beat_schedule:
            logger.info("✅ Celery beat schedule configured")
        else:
            logger.warning("⚠️ Celery beat schedule not configured")
        
        return True
    except Exception as e:
        logger.error(f"❌ Celery config error: {e}")
        return False

def main():
    """Run all tests"""
    logger.info("🧪 Testing GlobalCouponFinder Scraping Service")
    logger.info("=" * 60)
    
    tests = [
        ("Import Test", test_imports),
        ("Generic Scraper Test", test_generic_scraper),
        ("Affiliate Utils Test", test_affiliate_utils),
        ("Celery Config Test", test_celery_config),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        logger.info(f"\n🔍 Running {test_name}...")
        if test_func():
            passed += 1
        else:
            logger.error(f"❌ {test_name} failed")
    
    logger.info("\n" + "=" * 60)
    logger.info(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        logger.info("🎉 All tests passed! Ready for Railway deployment.")
        return True
    else:
        logger.error("❌ Some tests failed. Fix issues before deployment.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
