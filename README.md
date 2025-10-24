# GlobalCouponFinder

A comprehensive coupon scraping platform that aggregates discount codes from 50-100+ e-commerce sites across America, Europe, and Asia.

## 🌟 Features

- **Multi-Region Support**: America, Europe, Asia
- **Country Filtering**: Filter coupons by specific countries within each region
- **Food Delivery Coupons**: UberEats, DoorDash, Deliveroo, Foodpanda, Zomato, Swiggy, GrabFood
- **E-commerce Coupons**: Amazon, Walmart, Flipkart, Shopee, Lazada, and more
- **Hourly Scraping**: Automated scraping every hour for fresh coupons
- **Free Tier Backend**: All services run on free tiers (Supabase, Railway, Upstash, Vercel)

## 🛠️ Tech Stack

### Frontend
- Next.js 14 (React Framework)
- TypeScript
- Tailwind CSS
- Zustand (State Management)
- React Query (Data Fetching)
- Radix UI (Components)

### Backend
- FastAPI (Python)
- PostgreSQL (Supabase - Free)
- Redis (Upstash - Free)
- SQLAlchemy (ORM)
- Celery (Task Queue)

### Scrapers
- Python
- Playwright (Browser Automation)
- BeautifulSoup4
- Scrapy
- Fake User Agent

### Hosting
- Frontend: Vercel (Free)
- Backend API: Railway (Free $5 credit)
- Database: Supabase (Free PostgreSQL)
- Redis: Upstash (Free)
- Scrapers: Railway (Free)

## 💰 Monetization

1. **AdMob Ads**: Banner, Interstitial, Rewarded ads
2. **Affiliate Commissions**: Earn from coupon usage
3. **Freemium Subscription**: Premium features via Stripe

## 📁 Project Structure

```
E:\Projects\GlobalCouponFinder\
├── frontend\          # Next.js frontend
│   ├── src\
│   │   ├── app\       # Next.js 14 app directory
│   │   ├── components\
│   │   ├── lib\
│   │   ├── hooks\
│   │   └── types\
│   └── package.json
├── backend\           # FastAPI backend
│   ├── main.py
│   ├── config.py
│   ├── routers\
│   ├── models\
│   ├── schemas\
│   └── requirements.txt
├── scrapers\          # Python scraping service
│   ├── config.py
│   ├── scrapers\
│   └── utils\
└── docs\              # Documentation
```

## 🚀 Setup Instructions

### Prerequisites
- Node.js 18+ (Install to E:\Node)
- Python 3.11+ (Install to E:\Python311)
- Git (Install to E:\Git)

### Backend Setup

1. Navigate to backend directory:
```bash
cd E:\Projects\GlobalCouponFinder\backend
```

2. Activate virtual environment:
```bash
.\venv\Scripts\Activate.ps1
```

3. Run the development server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup (After Node.js installation)

1. Configure npm for E: drive:
```bash
npm config set cache E:\npm-cache
npm config set prefix E:\npm-global
```

2. Navigate to frontend directory:
```bash
cd E:\Projects\GlobalCouponFinder\frontend
```

3. Install dependencies:
```bash
npm install
```

4. Run development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 🌍 Supported Regions & Countries

### America
- United States (US)
- Canada (CA)
- Mexico (MX)

### Europe
- United Kingdom (GB)
- Germany (DE)
- France (FR)
- Italy (IT)
- Spain (ES)

### Asia
- India (IN)
- China (CN)
- Japan (JP)
- Singapore (SG)
- Thailand (TH)

## 📝 Environment Variables

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ADMOB_APP_ID=your-admob-app-id
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=your-stripe-public-key
```

### Backend (.env)
```
DATABASE_URL=your-supabase-postgresql-url
REDIS_URL=your-upstash-redis-url
SECRET_KEY=your-secret-key
STRIPE_SECRET_KEY=your-stripe-secret-key
```

## 🎯 Free Services Setup

1. **Supabase** (PostgreSQL): https://supabase.com - Free 500MB
2. **Railway** (Hosting): https://railway.app - Free $5 credit/month
3. **Upstash** (Redis): https://upstash.com - Free 10k commands/day
4. **Vercel** (Frontend): https://vercel.com - Free unlimited
5. **Resend** (Email): https://resend.com - Free 3,000 emails/month

## 📊 API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/regions` - Get all supported regions and countries
- `GET /api/coupons` - Get all coupons (with filters)
- `GET /api/coupons/{id}` - Get specific coupon
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login

## 🔧 Development

### Running Tests
```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm test
```

### Building for Production
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm run build
```

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📞 Support

For support, email support@globalcouponfinder.com or open an issue on GitHub.

