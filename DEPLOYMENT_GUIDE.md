# 🚀 GlobalCouponFinder - Complete Deployment Guide

## ✅ CURRENT STATUS

**COMPLETED:**
- ✅ Backend API (FastAPI) - Ready for Railway
- ✅ Scraping Service - Already running on Railway
- ✅ Database - 135 stores seeded in Supabase
- ✅ Frontend (Next.js) - Ready for Vercel
- ✅ Git repository - Clean and organized
- ✅ Premium features removed - Simplified to core functionality
- ✅ Maximum ads system - All users see ads

## 🎯 DEPLOYMENT PLAN

### 1. FRONTEND DEPLOYMENT (Vercel)

**Step 1: Push to GitHub**
```bash
cd E:\Projects\GlobalCouponFinder
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin master
```

**Step 2: Deploy to Vercel**
1. Go to https://vercel.com
2. Sign up/Login with GitHub
3. Click "New Project"
4. Import your GitHub repository
5. Framework: Next.js (auto-detected)
6. Root Directory: `frontend`
7. Build Command: `npm run build`
8. Output Directory: `.next`

**Step 3: Environment Variables**
Add these in Vercel dashboard → Settings → Environment Variables:

```
NEXT_PUBLIC_API_URL = https://your-backend.railway.app
NEXT_PUBLIC_ADMOB_APP_ID = ca-app-pub-9385746674842290~2532185877
NEXT_PUBLIC_ADMOB_BANNER_ID = ca-app-pub-9385746674842290/7749671776
NEXT_PUBLIC_ADMOB_INTERSTITIAL_ID = ca-app-pub-9385746674842290/2815967342
NEXT_PUBLIC_ADMOB_REWARDED_ID = ca-app-pub-9385746674842290/6615611556
```

### 2. BACKEND DEPLOYMENT (Railway)

**Step 1: Create Railway Project**
1. Go to https://railway.app
2. Sign up/Login with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Root Directory: `backend`

**Step 2: Environment Variables**
Add these in Railway dashboard:

```
DATABASE_URL = postgresql://postgres:[password]@db.xxx.supabase.co:5432/postgres
REDIS_URL = redis://default:xxx@redis-xxx.redis-cloud.com:xxx
SECRET_KEY = your-secret-key-here
DEBUG = false
```

**Step 3: Deploy**
Railway will automatically:
- Install Python dependencies
- Run the FastAPI server
- Expose your API URL

### 3. UPDATE FRONTEND API URL

After backend deployment:
1. Copy the Railway backend URL (e.g., `https://backend-xxx.railway.app`)
2. Update Vercel environment variable:
   - `NEXT_PUBLIC_API_URL = https://backend-xxx.railway.app`
3. Redeploy frontend

## 🔧 ENVIRONMENT VARIABLES SUMMARY

### Backend (Railway)
```
DATABASE_URL = postgresql://postgres:[password]@db.xxx.supabase.co:5432/postgres
REDIS_URL = redis://default:xxx@redis-xxx.redis-cloud.com:xxx
SECRET_KEY = your-secret-key-here
DEBUG = false
```

### Frontend (Vercel)
```
NEXT_PUBLIC_API_URL = https://backend-xxx.railway.app
NEXT_PUBLIC_ADMOB_APP_ID = ca-app-pub-9385746674842290~2532185877
NEXT_PUBLIC_ADMOB_BANNER_ID = ca-app-pub-9385746674842290/7749671776
NEXT_PUBLIC_ADMOB_INTERSTITIAL_ID = ca-app-pub-9385746674842290/2815967342
NEXT_PUBLIC_ADMOB_REWARDED_ID = ca-app-pub-9385746674842290/6615611556
```

### Scrapers (Already Running on Railway)
```
DATABASE_URL = postgresql://postgres:[password]@db.xxx.supabase.co:5432/postgres
REDIS_URL = redis://default:xxx@redis-xxx.redis-cloud.com:xxx
SCRAPE_FREQUENCY_MINUTES = 60
USE_PROXIES = false
HEADLESS = true
```

## 🎯 FINAL TESTING CHECKLIST

### After Deployment:
- [ ] Frontend loads on Vercel URL
- [ ] Backend API responds on Railway URL
- [ ] Database has 135 stores
- [ ] Coupons appear (wait 1-2 hours for scraping)
- [ ] Ads display on frontend
- [ ] Search functionality works
- [ ] Region/country filters work
- [ ] Mobile responsive

### Test URLs:
- Frontend: `https://your-app.vercel.app`
- Backend API: `https://your-backend.railway.app`
- API Health: `https://your-backend.railway.app/health`
- API Docs: `https://your-backend.railway.app/api/docs`

## 🚨 IMPORTANT NOTES

1. **Scraping Service**: Already running on Railway - DO NOT TOUCH
2. **Database**: Already seeded with 135 stores - DO NOT RESET
3. **Free Tier Limits**: 
   - Railway: $5/month free credit
   - Vercel: Unlimited for personal use
   - Supabase: 500MB database free
   - Upstash: 10,000 requests/day free

4. **Performance**: 
   - Frontend: Optimized for speed
   - Backend: Rate limited (60 req/min)
   - Scraping: 135 stores every hour
   - Ads: Maximum monetization

## 🎉 SUCCESS INDICATORS

**Your GlobalCouponFinder is working when:**
- ✅ Homepage loads with store/coupon grids
- ✅ Search returns results
- ✅ Region filters work (America/Europe/Asia)
- ✅ Country filters work
- ✅ Ads display on every page
- ✅ Coupons appear after 1-2 hours
- ✅ Mobile responsive design
- ✅ Fast loading times

## 🆘 TROUBLESHOOTING

**Frontend Issues:**
- Check Vercel build logs
- Verify environment variables
- Test API connection

**Backend Issues:**
- Check Railway logs
- Verify database connection
- Test API endpoints

**Scraping Issues:**
- Check Railway worker logs
- Verify Redis connection
- Monitor scrape_logs table

## 📊 MONITORING

**Railway Dashboard:**
- CPU/Memory usage
- Logs and errors
- Deployment status

**Vercel Dashboard:**
- Build status
- Performance metrics
- Analytics

**Supabase Dashboard:**
- Database size
- Query performance
- Real-time logs

---

## 🎯 NEXT STEPS

1. **Deploy Frontend to Vercel** (5 minutes)
2. **Deploy Backend to Railway** (10 minutes)
3. **Update API URLs** (2 minutes)
4. **Test Everything** (5 minutes)
5. **Wait for Coupons** (1-2 hours)

**Total Time: ~30 minutes + 2 hours for first coupons**

Your GlobalCouponFinder will be LIVE! 🚀💰
