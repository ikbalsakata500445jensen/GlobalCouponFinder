from pydantic_settings import BaseSettings
from typing import Optional
import os


class ScraperSettings(BaseSettings):
    """Scraper configuration settings"""
    
    # Scraper Configuration
    SCRAPER_USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    SCRAPER_TIMEOUT: int = 30
    SCRAPER_RETRY_ATTEMPTS: int = 3
    SCRAPER_DELAY_MIN: int = 1
    SCRAPER_DELAY_MAX: int = 3
    
    # API Configuration
    API_URL: str = "http://localhost:8000"
    API_KEY: Optional[str] = None
    
    # Database
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/couponfinder"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Playwright
    PLAYWRIGHT_BROWSERS_PATH: str = "E:\\playwright-browsers"
    
    # Environment
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = ScraperSettings()


# E-commerce sites to scrape by region
ECOMMERCE_SITES = {
    "america": {
        "US": [
            {"name": "Amazon", "url": "https://www.amazon.com", "type": "general"},
            {"name": "Walmart", "url": "https://www.walmart.com", "type": "general"},
            {"name": "Target", "url": "https://www.target.com", "type": "general"},
            {"name": "UberEats", "url": "https://www.ubereats.com", "type": "food"},
            {"name": "DoorDash", "url": "https://www.doordash.com", "type": "food"},
            {"name": "GrubHub", "url": "https://www.grubhub.com", "type": "food"},
        ],
        "CA": [
            {"name": "Amazon.ca", "url": "https://www.amazon.ca", "type": "general"},
            {"name": "Canadian Tire", "url": "https://www.canadiantire.ca", "type": "general"},
            {"name": "UberEats", "url": "https://www.ubereats.com/ca", "type": "food"},
        ],
        "MX": [
            {"name": "Amazon.mx", "url": "https://www.amazon.com.mx", "type": "general"},
            {"name": "UberEats", "url": "https://www.ubereats.com/mx", "type": "food"},
        ]
    },
    "europe": {
        "GB": [
            {"name": "Amazon.co.uk", "url": "https://www.amazon.co.uk", "type": "general"},
            {"name": "Tesco", "url": "https://www.tesco.com", "type": "general"},
            {"name": "Sainsbury's", "url": "https://www.sainsburys.co.uk", "type": "general"},
            {"name": "Deliveroo", "url": "https://deliveroo.co.uk", "type": "food"},
            {"name": "UberEats", "url": "https://www.ubereats.com/gb", "type": "food"},
        ],
        "DE": [
            {"name": "Amazon.de", "url": "https://www.amazon.de", "type": "general"},
            {"name": "MediaMarkt", "url": "https://www.mediamarkt.de", "type": "electronics"},
            {"name": "Lieferando", "url": "https://www.lieferando.de", "type": "food"},
        ],
        "FR": [
            {"name": "Amazon.fr", "url": "https://www.amazon.fr", "type": "general"},
            {"name": "Carrefour", "url": "https://www.carrefour.fr", "type": "general"},
            {"name": "UberEats", "url": "https://www.ubereats.com/fr", "type": "food"},
        ],
        "IT": [
            {"name": "Amazon.it", "url": "https://www.amazon.it", "type": "general"},
            {"name": "UberEats", "url": "https://www.ubereats.com/it", "type": "food"},
        ],
        "ES": [
            {"name": "Amazon.es", "url": "https://www.amazon.es", "type": "general"},
            {"name": "UberEats", "url": "https://www.ubereats.com/es", "type": "food"},
        ]
    },
    "asia": {
        "IN": [
            {"name": "Amazon.in", "url": "https://www.amazon.in", "type": "general"},
            {"name": "Flipkart", "url": "https://www.flipkart.com", "type": "general"},
            {"name": "Myntra", "url": "https://www.myntra.com", "type": "fashion"},
            {"name": "Zomato", "url": "https://www.zomato.com", "type": "food"},
            {"name": "Swiggy", "url": "https://www.swiggy.com", "type": "food"},
        ],
        "CN": [
            {"name": "Taobao", "url": "https://www.taobao.com", "type": "general"},
            {"name": "JD.com", "url": "https://www.jd.com", "type": "general"},
        ],
        "JP": [
            {"name": "Amazon.co.jp", "url": "https://www.amazon.co.jp", "type": "general"},
            {"name": "Rakuten", "url": "https://www.rakuten.co.jp", "type": "general"},
            {"name": "UberEats", "url": "https://www.ubereats.com/jp", "type": "food"},
        ],
        "SG": [
            {"name": "Lazada", "url": "https://www.lazada.sg", "type": "general"},
            {"name": "Shopee", "url": "https://shopee.sg", "type": "general"},
            {"name": "GrabFood", "url": "https://food.grab.com/sg", "type": "food"},
            {"name": "Foodpanda", "url": "https://www.foodpanda.sg", "type": "food"},
        ],
        "TH": [
            {"name": "Lazada", "url": "https://www.lazada.co.th", "type": "general"},
            {"name": "Shopee", "url": "https://shopee.co.th", "type": "general"},
            {"name": "GrabFood", "url": "https://food.grab.com/th", "type": "food"},
            {"name": "Foodpanda", "url": "https://www.foodpanda.co.th", "type": "food"},
        ]
    }
}

