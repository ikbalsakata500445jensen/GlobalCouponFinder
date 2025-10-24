from abc import ABC, abstractmethod
import requests
from typing import List, Dict
import random
import time
from fake_useragent import UserAgent
from config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseScraper(ABC):
    def __init__(self, store: Dict):
        self.store = store
        self.session = requests.Session()
        self.ua = UserAgent()
        self.config = store.get('scraper_config', {})
        
    def get_headers(self):
        """Generate realistic headers"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }
    
    def get_proxies(self):
        """Get proxy configuration if enabled"""
        if settings.USE_PROXIES and settings.PROXY_API_KEY:
            # ScraperAPI proxy format
            proxy_url = f"http://scraperapi:{settings.PROXY_API_KEY}@proxy-server.scraperapi.com:8001"
            return {
                'http': proxy_url,
                'https': proxy_url
            }
        return None
    
    def random_delay(self, min_seconds=None, max_seconds=None):
        """Add random delay between requests"""
        min_s = min_seconds or settings.MIN_DELAY_SECONDS
        max_s = max_seconds or settings.MAX_DELAY_SECONDS
        delay = random.uniform(min_s, max_s)
        logger.info(f"Waiting {delay:.2f} seconds...")
        time.sleep(delay)
    
    def make_request(self, url: str, method: str = 'GET', **kwargs):
        """Make HTTP request with retry logic"""
        for attempt in range(settings.RETRY_ATTEMPTS):
            try:
                logger.info(f"Request to {url} (attempt {attempt + 1})")
                
                response = self.session.request(
                    method=method,
                    url=url,
                    headers=self.get_headers(),
                    proxies=self.get_proxies(),
                    timeout=settings.REQUEST_TIMEOUT,
                    **kwargs
                )
                
                response.raise_for_status()
                return response
                
            except requests.RequestException as e:
                logger.warning(f"Request failed (attempt {attempt + 1}): {e}")
                
                if attempt < settings.RETRY_ATTEMPTS - 1:
                    self.random_delay(2, 5)
                else:
                    raise
    
    @abstractmethod
    def scrape(self) -> List[Dict]:
        """Scrape coupons from the store"""
        pass
    
    def parse_expiry_date(self, date_string: str):
        """Parse expiry date from various formats"""
        if not date_string:
            return None
        
        from dateutil import parser
        import re
        
        # Clean the date string
        date_string = date_string.strip()
        
        # Common patterns
        patterns = [
            (r'(\d{1,2})/(\d{1,2})/(\d{4})', '%m/%d/%Y'),  # MM/DD/YYYY
            (r'(\d{1,2})-(\d{1,2})-(\d{4})', '%m-%d-%Y'),  # MM-DD-YYYY
            (r'(\d{4})-(\d{1,2})-(\d{1,2})', '%Y-%m-%d'),  # YYYY-MM-DD
        ]
        
        for pattern, fmt in patterns:
            match = re.search(pattern, date_string)
            if match:
                try:
                    from datetime import datetime
                    return datetime.strptime(match.group(0), fmt)
                except:
                    pass
        
        # Try generic parser
        try:
            return parser.parse(date_string)
        except:
            logger.warning(f"Could not parse date: {date_string}")
            return None
    
    def parse_discount(self, discount_string: str):
        """Extract numeric discount value"""
        if not discount_string:
            return None, None
        
        import re
        
        # Look for percentage: 20% OFF, 20% discount
        percentage_match = re.search(r'(\d+(?:\.\d+)?)\s*%', discount_string)
        if percentage_match:
            return float(percentage_match.group(1)), 'percentage'
        
        # Look for fixed amount: $10 OFF, $10 discount
        amount_match = re.search(r'\$(\d+(?:\.\d+)?)', discount_string)
        if amount_match:
            return float(amount_match.group(1)), 'fixed'
        
        # Look for just numbers
        number_match = re.search(r'(\d+(?:\.\d+)?)', discount_string)
        if number_match:
            return float(number_match.group(1)), None
        
        return None, None
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        if not text:
            return ""
        
        import re
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Strip leading/trailing whitespace
        text = text.strip()
        
        return text