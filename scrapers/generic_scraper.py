from base_scraper import BaseScraper
from bs4 import BeautifulSoup
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class GenericCouponScraper(BaseScraper):
    """
    Generic HTML scraper using BeautifulSoup
    Works for most static websites
    """
    
    def scrape(self) -> List[Dict]:
        coupons = []
        
        try:
            url = self.config.get('coupon_list_url')
            if not url:
                logger.error(f"No coupon_list_url configured for {self.store['name']}")
                return []
            
            logger.info(f"Scraping {self.store['name']} at {url}")
            
            # Fetch the page
            response = self.make_request(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get selectors from config
            selectors = self.config.get('selectors', {})
            container_selector = selectors.get('coupon_container')
            
            if not container_selector:
                logger.error(f"No coupon_container selector for {self.store['name']}")
                return []
            
            # Find all coupon containers
            containers = soup.select(container_selector)
            logger.info(f"Found {len(containers)} coupon containers")
            
            for container in containers:
                try:
                    coupon = self.extract_coupon_data(container, selectors)
                    
                    # Validate coupon has required fields
                    if coupon and coupon.get('code'):
                        coupons.append(coupon)
                        logger.debug(f"Extracted coupon: {coupon['code']}")
                    
                except Exception as e:
                    logger.warning(f"Error extracting coupon: {e}")
                    continue
                
                # Random delay between coupons
                self.random_delay(0.5, 1.5)
            
            logger.info(f"Successfully scraped {len(coupons)} coupons from {self.store['name']}")
            
        except Exception as e:
            logger.error(f"Error scraping {self.store['name']}: {e}")
            raise
        
        return coupons
    
    def extract_coupon_data(self, container, selectors: Dict) -> Dict:
        """Extract coupon data from HTML container"""
        
        # Extract code (required)
        code_elem = container.select_one(selectors.get('code', ''))
        if not code_elem:
            return None
        
        code = self.clean_text(code_elem.get_text())
        
        # Extract title
        title_elem = container.select_one(selectors.get('title', ''))
        title = self.clean_text(title_elem.get_text()) if title_elem else 'Discount Code'
        
        # Extract description
        desc_elem = container.select_one(selectors.get('description', ''))
        description = self.clean_text(desc_elem.get_text()) if desc_elem else None
        
        # Extract expiry date
        expiry_elem = container.select_one(selectors.get('expiry', ''))
        expiry_text = self.clean_text(expiry_elem.get_text()) if expiry_elem else None
        expires_at = self.parse_expiry_date(expiry_text) if expiry_text else None
        
        # Extract discount
        discount_elem = container.select_one(selectors.get('discount', ''))
        discount_text = self.clean_text(discount_elem.get_text()) if discount_elem else None
        discount_value, discount_type = self.parse_discount(discount_text) if discount_text else (None, None)
        
        # Build coupon object
        coupon = {
            'code': code,
            'title': title,
            'description': description,
            'expires_at': expires_at,
            'discount_value': discount_value,
            'discount_type': discount_type or 'percentage',
            'source_url': self.config.get('coupon_list_url'),
        }
        
        return coupon
