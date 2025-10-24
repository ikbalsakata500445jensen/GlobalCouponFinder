import urllib.parse
from typing import Dict

def generate_affiliate_url(store: Dict, coupon_data: Dict = None) -> str:
    """
    Generate affiliate tracking URL based on store's affiliate network
    """
    base_url = f"https://{store['domain']}"
    affiliate_network = store.get('affiliate_network', '')
    affiliate_id = store.get('affiliate_id', '')
    merchant_id = store.get('merchant_id', '')
    
    # ShareASale
    if affiliate_network == 'shareasale':
        return f"https://shareasale.com/r.cfm?b={merchant_id}&u=YOUR_SHAREASALE_ID&m={merchant_id}&urllink={urllib.parse.quote(base_url)}"
    
    # CJ Affiliate (Commission Junction)
    elif affiliate_network == 'cj':
        return f"https://www.anrdoezrs.net/click-YOUR_CJ_ID-{merchant_id}?url={urllib.parse.quote(base_url)}"
    
    # Rakuten Advertising
    elif affiliate_network == 'rakuten':
        return f"https://click.linksynergy.com/deeplink?id=YOUR_RAKUTEN_ID&mid={merchant_id}&murl={urllib.parse.quote(base_url)}"
    
    # Amazon Associates
    elif affiliate_network == 'amazon':
        region_tags = {
            'america': 'yourtag-20',
            'europe': 'yourtag-21',
            'asia': 'yourtag-21'
        }
        tag = region_tags.get(store.get('region', 'america'), 'yourtag-20')
        return f"{base_url}?tag={tag}"
    
    # Impact
    elif affiliate_network == 'impact':
        return f"https://impact.com/YOUR_IMPACT_ID?campaignId={merchant_id}&destURL={urllib.parse.quote(base_url)}"
    
    # Awin
    elif affiliate_network == 'awin':
        return f"https://www.awin1.com/cread.php?awinmid={merchant_id}&awinaffid=YOUR_AWIN_ID&ued={urllib.parse.quote(base_url)}"
    
    # Shopee Affiliate
    elif affiliate_network == 'shopee':
        return f"{base_url}?af_siteid=YOUR_SHOPEE_ID"
    
    # Lazada Affiliate
    elif affiliate_network == 'lazada':
        return f"{base_url}?spm=YOUR_LAZADA_ID"
    
    # Flipkart Affiliate
    elif affiliate_network == 'flipkart':
        return f"{base_url}?affid=YOUR_FLIPKART_ID"
    
    # Default: return base URL
    else:
        return base_url
