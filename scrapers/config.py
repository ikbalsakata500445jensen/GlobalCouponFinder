from pydantic_settings import BaseSettings
from typing import Optional

class ScraperSettings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Scraping settings
    SCRAPE_FREQUENCY_MINUTES: int = 60
    MAX_CONCURRENT_SCRAPERS: int = 5
    REQUEST_TIMEOUT: int = 30
    RETRY_ATTEMPTS: int = 3
    
    # Anti-detection
    MIN_DELAY_SECONDS: float = 1.0
    MAX_DELAY_SECONDS: float = 3.0
    USE_PROXIES: bool = False
    PROXY_API_KEY: Optional[str] = None
    
    # Playwright
    PLAYWRIGHT_BROWSERS_PATH: str = "/tmp/playwright-browsers"
    HEADLESS: bool = True
    
    class Config:
        env_file = ".env"

settings = ScraperSettings()