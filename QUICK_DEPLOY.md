# 🚀 QUICK DEPLOYMENT - 5 MINUTES

## IMMEDIATE ACTIONS

### 1. DEPLOY FRONTEND (Vercel) - 2 minutes
```bash
cd E:\Projects\GlobalCouponFinder\frontend
npx vercel login
npx vercel
```
- Follow prompts (use defaults)
- Copy the generated URL

### 2. DEPLOY BACKEND (Railway) - 3 minutes
```bash
cd E:\Projects\GlobalCouponFinder\backend
# Push to GitHub first
git add .
git commit -m "Backend ready for deployment"
git push origin master
```

Then:
1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Select your repo
4. Root Directory: `backend`
5. Add environment variables (see below)

### 3. UPDATE FRONTEND API URL
1. Copy Railway backend URL
2. Update Vercel environment variable: `NEXT_PUBLIC_API_URL`
3. Redeploy frontend

## ENVIRONMENT VARIABLES

### Railway (Backend):
```
DATABASE_URL = postgresql://postgres:[password]@db.xxx.supabase.co:5432/postgres
REDIS_URL = redis://default:xxx@redis-xxx.redis-cloud.com:xxx
SECRET_KEY = your-secret-key-here
```

### Vercel (Frontend):
```
NEXT_PUBLIC_API_URL = https://your-backend.railway.app
NEXT_PUBLIC_ADMOB_APP_ID = ca-app-pub-9385746674842290~2532185877
NEXT_PUBLIC_ADMOB_BANNER_ID = ca-app-pub-9385746674842290/7749671776
NEXT_PUBLIC_ADMOB_INTERSTITIAL_ID = ca-app-pub-9385746674842290/2815967342
NEXT_PUBLIC_ADMOB_REWARDED_ID = ca-app-pub-9385746674842290/6615611556
```

## ✅ DONE!

Your GlobalCouponFinder will be LIVE in 5 minutes! 🎉

**Test URLs:**
- Frontend: `https://your-app.vercel.app`
- Backend: `https://your-backend.railway.app/health`
- API Docs: `https://your-backend.railway.app/api/docs`

**Scraping:** Already running on Railway (135 stores every hour)
**Database:** Already seeded with 135 stores
**Coupons:** Will appear in 1-2 hours
