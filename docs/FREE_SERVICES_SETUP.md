# Free Backend Services Setup Guide

This guide will help you set up all the free backend services required for GlobalCouponFinder.

## 1. Supabase (PostgreSQL Database) - FREE

**Free Tier**: 500MB database, 2GB bandwidth, 50MB file storage

### Setup Steps:

1. **Create Account**:
   - Visit: https://supabase.com
   - Sign up with GitHub or email
   - Create a new project

2. **Get Credentials**:
   - Go to Project Settings > Database
   - Copy the connection string (URI format)
   - Example: `postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres`

3. **Update Backend .env**:
   ```env
   DATABASE_URL=postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres
   SUPABASE_URL=https://[project-ref].supabase.co
   SUPABASE_KEY=[your-anon-key]
   ```

4. **Run Migrations**:
   ```bash
   cd E:\Projects\GlobalCouponFinder\backend
   .\venv\Scripts\Activate.ps1
   alembic upgrade head
   ```

## 2. Upstash (Redis) - FREE

**Free Tier**: 10,000 commands/day, 256MB storage

### Setup Steps:

1. **Create Account**:
   - Visit: https://upstash.com
   - Sign up with GitHub or email
   - Create a new Redis database

2. **Get Credentials**:
   - Select your database
   - Copy the Redis URL
   - Example: `redis://default:[password]@[endpoint].upstash.io:6379`

3. **Update Backend .env**:
   ```env
   REDIS_URL=redis://default:[password]@[endpoint].upstash.io:6379
   UPSTASH_REDIS_URL=redis://default:[password]@[endpoint].upstash.io:6379
   ```

## 3. Railway (Backend Hosting) - FREE

**Free Tier**: $5 credit/month (enough for small projects)

### Setup Steps:

1. **Create Account**:
   - Visit: https://railway.app
   - Sign up with GitHub
   - Connect your GitHub repository

2. **Deploy Backend**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose GlobalCouponFinder repository
   - Select backend folder
   - Add environment variables from .env

3. **Configure Build**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Watch Paths: `backend/**`

4. **Get URL**:
   - Copy the generated URL (e.g., `https://[app-name].up.railway.app`)
   - Update frontend .env:
     ```env
     NEXT_PUBLIC_API_URL=https://[app-name].up.railway.app
     ```

## 4. Vercel (Frontend Hosting) - FREE

**Free Tier**: Unlimited sites, 100GB bandwidth

### Setup Steps:

1. **Create Account**:
   - Visit: https://vercel.com
   - Sign up with GitHub
   - Import GlobalCouponFinder repository

2. **Configure Project**:
   - Framework Preset: Next.js
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `.next`

3. **Add Environment Variables**:
   - Go to Project Settings > Environment Variables
   - Add all variables from frontend/.env.example

4. **Deploy**:
   - Click "Deploy"
   - Your site will be live at: `https://[project-name].vercel.app`

## 5. Resend (Email Service) - FREE

**Free Tier**: 3,000 emails/month, 100 emails/day

### Setup Steps:

1. **Create Account**:
   - Visit: https://resend.com
   - Sign up with email
   - Verify your domain (optional, can use test domain)

2. **Get API Key**:
   - Go to API Keys
   - Create new API key
   - Copy the key

3. **Update Backend .env**:
   ```env
   RESEND_API_KEY=re_[your-api-key]
   ```

## 6. Stripe (Payments) - FREE for Testing

**Free Tier**: Free for testing, 2.9% + $0.30 per transaction in production

### Setup Steps:

1. **Create Account**:
   - Visit: https://stripe.com
   - Sign up for free account
   - Complete business verification (optional for testing)

2. **Get Test Keys**:
   - Go to Developers > API Keys
   - Copy Test Publishable Key and Test Secret Key

3. **Update Environment Variables**:
   
   Backend .env:
   ```env
   STRIPE_SECRET_KEY=sk_test_[your-secret-key]
   STRIPE_WEBHOOK_SECRET=whsec_[your-webhook-secret]
   ```
   
   Frontend .env.local:
   ```env
   NEXT_PUBLIC_STRIPE_PUBLIC_KEY=pk_test_[your-publishable-key]
   ```

4. **Setup Webhooks** (Optional):
   - Go to Developers > Webhooks
   - Add endpoint: `https://[your-api-url]/api/webhooks/stripe`
   - Select events: `checkout.session.completed`, `payment_intent.succeeded`

## 7. Google AdMob (Monetization) - FREE

**Revenue**: Earn from ads displayed in your app

### Setup Steps:

1. **Create Account**:
   - Visit: https://admob.google.com
   - Sign in with Google account
   - Accept terms and conditions

2. **Create App**:
   - Click "Apps" > "Add App"
   - Enter app details
   - Choose platform (Web/Android/iOS)

3. **Create Ad Units**:
   - Banner Ad
   - Interstitial Ad
   - Rewarded Ad

4. **Update Frontend .env.local**:
   ```env
   NEXT_PUBLIC_ADMOB_APP_ID=ca-app-pub-XXXXX~XXXXX
   NEXT_PUBLIC_ADMOB_BANNER_ID=ca-app-pub-XXXXX/BANNER
   NEXT_PUBLIC_ADMOB_INTERSTITIAL_ID=ca-app-pub-XXXXX/INTERSTITIAL
   NEXT_PUBLIC_ADMOB_REWARDED_ID=ca-app-pub-XXXXX/REWARDED
   ```

## Cost Summary

| Service | Free Tier | Monthly Cost (Free) |
|---------|-----------|---------------------|
| Supabase | 500MB DB | $0 |
| Upstash Redis | 10k commands/day | $0 |
| Railway | $5 credit | $0 |
| Vercel | Unlimited | $0 |
| Resend | 3,000 emails | $0 |
| Stripe | Testing | $0 |
| AdMob | Revenue-based | Earn money |
| **TOTAL** | - | **$0** |

## Post-Setup Checklist

- [ ] Supabase database created and connected
- [ ] Upstash Redis created and connected
- [ ] Railway backend deployed
- [ ] Vercel frontend deployed
- [ ] Resend email configured
- [ ] Stripe test mode configured
- [ ] AdMob account created
- [ ] All environment variables updated
- [ ] Test backend API endpoints
- [ ] Test frontend connection
- [ ] Test email sending
- [ ] Test payment flow

## Testing

### Test Backend Connection
```bash
curl https://[your-railway-url]/health
# Should return: {"status": "healthy"}
```

### Test Frontend
Visit: `https://[your-vercel-url]`
Should display the GlobalCouponFinder homepage

### Test Database
```bash
curl https://[your-railway-url]/api/regions
# Should return list of regions
```

## Monitoring & Limits

### Supabase
- Monitor usage in Dashboard > Database > Usage
- Upgrade to Pro ($25/mo) if you exceed limits

### Upstash Redis
- Monitor commands in Dashboard
- Upgrade to paid plan if you exceed 10k commands/day

### Railway
- Monitor $5 credit usage in Dashboard
- Add payment method for continuous service

### Vercel
- Monitor bandwidth in Dashboard > Usage
- Free tier includes 100GB bandwidth/month

## Support

If you encounter issues:

1. **Supabase**: https://supabase.com/docs
2. **Upstash**: https://docs.upstash.com
3. **Railway**: https://docs.railway.app
4. **Vercel**: https://vercel.com/docs
5. **Resend**: https://resend.com/docs
6. **Stripe**: https://stripe.com/docs

