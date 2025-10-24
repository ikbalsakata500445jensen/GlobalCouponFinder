from base_scraper import BaseScraper
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from typing import List, Dict
import logging
from config import settings

logger = logging.getLogger(__name__)

class JavaScriptCouponScraper(BaseScraper):
    """
    JavaScript-heavy website scraper using Playwright
    Works for dynamic sites that load content via JS
    """
    
    def scrape(self) -> List[Dict]:
        coupons = []
        
        try:
            url = self.config.get('coupon_list_url')
            if not url:
                logger.error(f"No coupon_list_url configured for {self.store['name']}")
                return []
            
            logger.info(f"Scraping {self.store['name']} with Playwright at {url}")
            
            with sync_playwright() as p:
                # Launch browser
                browser = p.chromium.launch(
                    headless=settings.HEADLESS,
                    args=[
                        '--no-sandbox',
                        '--disable-setuid-sandbox',
                        '--disable-dev-shm-usage',
                        '--disable-gpu',
                    ]
                )
                
                # Create context with realistic settings
                context = browser.new_context(
                    user_agent=self.ua.random,
                    viewport={'width': 1920, 'height': 1080},
                    locale='en-US',
                )
                
                # Create page
                page = context.new_page()
                
                try:
                    # Navigate to page
                    page.goto(url, wait_until='networkidle', timeout=30000)
                    
                    # Wait for coupon containers to load
                    selectors = self.config.get('selectors', {})
                    container_selector = selectors.get('coupon_container')
                    
                    if container_selector:
                        page.wait_for_selector(container_selector, timeout=10000)
                    
                    # Handle pagination if needed
                    pagination_type = self.config.get('pagination', {}).get('type')
                    if pagination_type == 'scroll':
                        self.scroll_to_bottom(page)
                    elif pagination_type == 'button':
                        self.click_load_more(page)
                    
                    # Extract coupons
                    coupons = self.extract_coupons_from_page(page, selectors)
                    
                    logger.info(f"Successfully scraped {len(coupons)} coupons from {self.store['name']}")
                
                except PlaywrightTimeout as e:
                    logger.error(f"Timeout scraping {self.store['name']}: {e}")
                
                finally:
                    browser.close()
        
        except Exception as e:
            logger.error(f"Error scraping {self.store['name']}: {e}")
            raise
        
        return coupons
    
    def scroll_to_bottom(self, page):
        """Scroll to load lazy-loaded content"""
        logger.info("Scrolling to load more content...")
        
        page.evaluate("""
            async () => {
                await new Promise((resolve) => {
                    let totalHeight = 0;
                    const distance = 100;
                    const timer = setInterval(() => {
                        const scrollHeight = document.body.scrollHeight;
                        window.scrollBy(0, distance);
                        totalHeight += distance;
                        
                        if(totalHeight >= scrollHeight){
                            clearInterval(timer);
                            resolve();
                        }
                    }, 100);
                });
            }
        """)
        
        # Wait for content to load
        page.wait_for_timeout(2000)
    
    def click_load_more(self, page):
        """Click 'Load More' button if exists"""
        load_more_selector = self.config.get('pagination', {}).get('button_selector', '.load-more')
        
        try:
            max_clicks = self.config.get('pagination', {}).get('max_clicks', 5)
            clicks = 0
            
            while clicks < max_clicks:
                button = page.query_selector(load_more_selector)
                if button and button.is_visible():
                    button.click()
                    page.wait_for_timeout(2000)
                    clicks += 1
                else:
                    break
            
            logger.info(f"Clicked 'Load More' {clicks} times")
        
        except Exception as e:
            logger.warning(f"Error clicking load more: {e}")
    
    def extract_coupons_from_page(self, page, selectors: Dict) -> List[Dict]:
        """Extract coupons from Playwright page"""
        coupons = []
        
        container_selector = selectors.get('coupon_container')
        if not container_selector:
            logger.error("No coupon_container selector")
            return []
        
        # Get all coupon containers
        containers = page.query_selector_all(container_selector)
        logger.info(f"Found {len(containers)} coupon containers")
        
        for container in containers:
            try:
                # Extract code
                code_elem = container.query_selector(selectors.get('code', ''))
                if not code_elem:
                    continue
                
                code = self.clean_text(code_elem.inner_text())
                
                # Extract title
                title_elem = container.query_selector(selectors.get('title', ''))
                title = self.clean_text(title_elem.inner_text()) if title_elem else 'Discount Code'
                
                # Extract description
                desc_elem = container.query_selector(selectors.get('description', ''))
                description = self.clean_text(desc_elem.inner_text()) if desc_elem else None
                
                # Extract expiry
                expiry_elem = container.query_selector(selectors.get('expiry', ''))
                expiry_text = self.clean_text(expiry_elem.inner_text()) if expiry_elem else None
                expires_at = self.parse_expiry_date(expiry_text) if expiry_text else None
                
                # Extract discount
                discount_elem = container.query_selector(selectors.get('discount', ''))
                discount_text = self.clean_text(discount_elem.inner_text()) if discount_elem else None
                discount_value, discount_type = self.parse_discount(discount_text) if discount_text else (None, None)
                
                coupon = {
                    'code': code,
                    'title': title,
                    'description': description,
                    'expires_at': expires_at,
                    'discount_value': discount_value,
                    'discount_type': discount_type or 'percentage',
                    'source_url': self.config.get('coupon_list_url'),
                }
                
                coupons.append(coupon)
                
            except Exception as e:
                logger.warning(f"Error extracting coupon: {e}")
                continue
        
        return coupons
