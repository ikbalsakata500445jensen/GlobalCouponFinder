"""
Base scraper class for GlobalCouponFinder
All site-specific scrapers should inherit from this class
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import logging
import time
import random
from datetime import datetime
from playwright.sync_api import sync_playwright, Page, Browser
from fake_useragent import UserAgent
from config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BaseScraper(ABC):
    """Base class for all coupon scrapers"""
    
    def __init__(self, site_name: str, site_url: str, country: str, region: str):
        self.site_name = site_name
        self.site_url = site_url
        self.country = country
        self.region = region
        self.user_agent = UserAgent()
        self.coupons: List[Dict] = []
        
    def get_random_user_agent(self) -> str:
        """Get a random user agent string"""
        return self.user_agent.random
    
    def random_delay(self):
        """Add a random delay to avoid rate limiting"""
        delay = random.uniform(
            settings.SCRAPER_DELAY_MIN,
            settings.SCRAPER_DELAY_MAX
        )
        time.sleep(delay)
    
    def scrape_with_retry(self, max_attempts: int = None) -> List[Dict]:
        """Scrape with retry logic"""
        max_attempts = max_attempts or settings.SCRAPER_RETRY_ATTEMPTS
        
        for attempt in range(max_attempts):
            try:
                logger.info(f"Scraping {self.site_name} (Attempt {attempt + 1}/{max_attempts})")
                coupons = self.scrape()
                logger.info(f"Successfully scraped {len(coupons)} coupons from {self.site_name}")
                return coupons
            
            except Exception as e:
                logger.error(f"Error scraping {self.site_name} (Attempt {attempt + 1}): {str(e)}")
                
                if attempt < max_attempts - 1:
                    logger.info(f"Retrying in {settings.SCRAPER_DELAY_MAX} seconds...")
                    time.sleep(settings.SCRAPER_DELAY_MAX)
                else:
                    logger.error(f"Failed to scrape {self.site_name} after {max_attempts} attempts")
                    return []
    
    @abstractmethod
    def scrape(self) -> List[Dict]:
        """
        Main scraping method - must be implemented by subclasses
        
        Returns:
            List of coupon dictionaries with the following structure:
            {
                'code': str,
                'title': str,
                'description': str,
                'discount_type': str,  # 'percentage', 'fixed_amount', 'free_shipping'
                'discount_value': float,
                'min_purchase': float or None,
                'expiry_date': datetime or None,
                'site_name': str,
                'site_url': str,
                'country': str,
                'region': str,
                'category': str,  # 'food', 'general', 'fashion', 'electronics'
                'verified': bool,
                'scraped_at': datetime
            }
        """
        pass
    
    def create_coupon_dict(
        self,
        code: str,
        title: str,
        description: str = "",
        discount_type: str = "percentage",
        discount_value: float = 0.0,
        min_purchase: Optional[float] = None,
        expiry_date: Optional[datetime] = None,
        category: str = "general",
        verified: bool = False
    ) -> Dict:
        """Helper method to create a standardized coupon dictionary"""
        
        return {
            'code': code.strip().upper(),
            'title': title.strip(),
            'description': description.strip(),
            'discount_type': discount_type,
            'discount_value': discount_value,
            'min_purchase': min_purchase,
            'expiry_date': expiry_date,
            'site_name': self.site_name,
            'site_url': self.site_url,
            'country': self.country,
            'region': self.region,
            'category': category,
            'verified': verified,
            'scraped_at': datetime.utcnow()
        }


class PlaywrightScraper(BaseScraper):
    """Base scraper using Playwright for JavaScript-heavy sites"""
    
    def __init__(self, site_name: str, site_url: str, country: str, region: str):
        super().__init__(site_name, site_url, country, region)
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None
    
    def start_browser(self):
        """Start Playwright browser"""
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        context = self.browser.new_context(
            user_agent=self.get_random_user_agent(),
            viewport={'width': 1920, 'height': 1080}
        )
        self.page = context.new_page()
        self.page.set_default_timeout(settings.SCRAPER_TIMEOUT * 1000)
    
    def stop_browser(self):
        """Stop Playwright browser"""
        if self.browser:
            self.browser.close()
    
    def navigate_to_page(self, url: str):
        """Navigate to a URL"""
        if not self.page:
            self.start_browser()
        
        logger.info(f"Navigating to {url}")
        self.page.goto(url, wait_until='networkidle')
        self.random_delay()
    
    def scrape(self) -> List[Dict]:
        """Override this method in subclasses"""
        try:
            self.start_browser()
            coupons = self._scrape_implementation()
            return coupons
        finally:
            self.stop_browser()
    
    @abstractmethod
    def _scrape_implementation(self) -> List[Dict]:
        """Implement the actual scraping logic here"""
        pass


# Example scraper implementation
class AmazonScraper(PlaywrightScraper):
    """Example scraper for Amazon coupons"""
    
    def _scrape_implementation(self) -> List[Dict]:
        """Scrape Amazon coupons"""
        coupons = []
        
        # Navigate to coupons page
        coupons_url = f"{self.site_url}/coupons"
        self.navigate_to_page(coupons_url)
        
        # This is a placeholder - actual implementation would parse the page
        # and extract coupon data
        
        # Example coupon (remove this in production)
        coupon = self.create_coupon_dict(
            code="AMAZON20",
            title="20% Off Electronics",
            description="Get 20% off on selected electronics",
            discount_type="percentage",
            discount_value=20.0,
            category="electronics",
            verified=True
        )
        coupons.append(coupon)
        
        return coupons


if __name__ == "__main__":
    # Example usage
    scraper = AmazonScraper(
        site_name="Amazon",
        site_url="https://www.amazon.com",
        country="US",
        region="america"
    )
    
    coupons = scraper.scrape_with_retry()
    
    for coupon in coupons:
        print(f"Code: {coupon['code']}")
        print(f"Title: {coupon['title']}")
        print(f"Discount: {coupon['discount_value']}%")
        print("---")

