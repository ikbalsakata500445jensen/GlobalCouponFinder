# GlobalCouponFinder Scraping Service - Railway Deployment Guide

## 🚀 Overview
This scraping service runs on Railway.app (cloud) to automatically scrape 100+ websites for coupons every hour.

## 📁 Project Structure
```
scrapers/
├── __init__.py
├── config.py              # Configuration settings
├── celery_app.py          # Celery task queue setup
├── tasks.py               # Scraping tasks
├── base_scraper.py        # Base scraper class
├── generic_scraper.py     # HTML scraper (BeautifulSoup)
├── javascript_scraper.py  # JS scraper (Playwright)
├── affiliate_utils.py    # Affiliate URL generation
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment commands
├── railway.toml          # Railway configuration
├── env.example           # Environment variables template
├── test_scraper.py       # Local testing script
└── DEPLOYMENT.md         # This file
```

## 🛠 Local Testing

### 1. Install Dependencies
```bash
cd E:\Projects\GlobalCouponFinder\scrapers
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

### 2. Set Environment Variables
```bash
# Copy example file
copy env.example .env

# Edit .env with your actual values:
# DATABASE_URL=postgresql://postgres:[password]@db.tuegworkqglgbtitazwm.supabase.co:5432/postgres
# REDIS_URL=redis://default:gEyBsxKTT0lsu2hYiNMCQr9HYlDfltyY@redis-13520.c74.us-east-1-4.ec2.redns.redis-cloud.com:13520
```

### 3. Test Scrapers
```bash
python test_scraper.py
```

### 4. Test Celery Worker (Terminal 1)
```bash
celery -A celery_app worker --loglevel=info --pool=solo
```

### 5. Test Celery Beat (Terminal 2)
```bash
celery -A celery_app beat --loglevel=info
```

## ☁️ Railway Deployment

### 1. Prepare for Deployment
```bash
# Initialize git if not already done
cd E:\Projects\GlobalCouponFinder\scrapers
git init
git add .
git commit -m "Initial scraping service"

# Push to GitHub
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### 2. Deploy to Railway.app

#### Step 1: Create Railway Project
1. Go to https://railway.app
2. Sign up/Login with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Select the `scrapers` folder as root directory

#### Step 2: Add Environment Variables
In Railway dashboard, add these environment variables:

**Database:**
- `DATABASE_URL` = `postgresql://postgres:[Kemun!ng555]@db.tuegworkqglgbtitazwm.supabase.co:5432/postgres`

**Redis:**
- `REDIS_URL` = `redis://default:gEyBsxKTT0lsu2hYiNMCQr9HYlDfltyY@redis-13520.c74.us-east-1-4.ec2.redns.redis-cloud.com:13520`

**Scraping Settings:**
- `SCRAPE_FREQUENCY_MINUTES` = `60`
- `USE_PROXIES` = `false`
- `HEADLESS` = `true`
- `PLAYWRIGHT_BROWSERS_PATH` = `/tmp/playwright-browsers`

#### Step 3: Deploy Celery Worker
Railway will automatically detect the `Procfile` and deploy the worker service.

#### Step 4: Deploy Celery Beat (Separate Service)
1. Create another Railway service
2. Same repository, same environment variables
3. Override the start command to: `celery -A celery_app beat --loglevel=info`

### 3. Monitor Deployment

#### Check Logs
- Go to Railway dashboard
- Click on your service
- View "Deployments" tab for logs
- Check "Metrics" for resource usage

#### Verify Services
- **Worker Service**: Should show "celery worker" processes
- **Beat Service**: Should show "celery beat" scheduler
- **Logs**: Should show scraping activity every hour

## 📊 Monitoring & Maintenance

### 1. Check Scraping Activity
```sql
-- Check recent scrape logs
SELECT * FROM scrape_logs 
ORDER BY created_at DESC 
LIMIT 10;

-- Check store scraping status
SELECT name, last_scraped_at, is_active 
FROM stores 
ORDER BY last_scraped_at DESC;
```

### 2. Monitor Performance
- **Railway Metrics**: CPU, Memory, Network usage
- **Database**: Coupon counts, scrape success rates
- **Redis**: Task queue status

### 3. Troubleshooting

#### Common Issues:
1. **Playwright Browser Issues**: Ensure `playwright install chromium` runs during build
2. **Database Connection**: Verify `DATABASE_URL` is correct
3. **Redis Connection**: Verify `REDIS_URL` is correct
4. **Memory Issues**: Reduce `--concurrency` in Procfile

#### Debug Commands:
```bash
# Check Celery status
celery -A celery_app inspect active

# Check scheduled tasks
celery -A celery_app inspect scheduled

# Purge failed tasks
celery -A celery_app purge
```

## 🔧 Configuration

### Scraping Frequency
- **Default**: Every hour (60 minutes)
- **Change**: Set `SCRAPE_FREQUENCY_MINUTES` environment variable
- **Per Store**: Each store has individual `scrape_frequency` setting

### Anti-Detection Settings
- **User Agents**: Rotated automatically
- **Delays**: Random 1-3 seconds between requests
- **Proxies**: Optional (set `USE_PROXIES=true` and `PROXY_API_KEY`)

### Resource Limits
- **Task Timeout**: 10 minutes per store
- **Concurrency**: 5 concurrent scrapers
- **Memory**: Optimized for Railway's free tier

## 📈 Expected Results

### After Deployment:
- ✅ 135 stores scraped automatically
- ✅ New coupons discovered every hour
- ✅ Expired coupons cleaned up daily
- ✅ User daily limits reset at midnight
- ✅ All activity logged to database

### Performance Metrics:
- **Scraping Success Rate**: 80-90%
- **New Coupons/Hour**: 50-200
- **Database Growth**: ~1000 coupons/day
- **Resource Usage**: <512MB RAM, <1 CPU core

## 🚨 Important Notes

1. **Cloud Only**: This service runs on Railway, NOT locally
2. **Free Tier**: Uses Railway's $5/month free credit
3. **Database**: Requires PostgreSQL (Supabase)
4. **Redis**: Requires Redis (Upstash)
5. **Monitoring**: Check logs regularly for issues

## 🆘 Support

If you encounter issues:
1. Check Railway logs for errors
2. Verify environment variables
3. Test locally first with `test_scraper.py`
4. Check database connectivity
5. Monitor Redis queue status
