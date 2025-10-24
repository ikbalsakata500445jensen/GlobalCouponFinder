# GlobalCouponFinder Frontend - Vercel Deployment Guide

## 🚀 Deploy to Vercel

### 1. **Prepare for Deployment**

The frontend is ready for Vercel deployment with:
- ✅ Next.js 14 with App Router
- ✅ TypeScript configuration
- ✅ Tailwind CSS styling
- ✅ All components and pages created
- ✅ AdMob integration (disabled for testing)

### 2. **Deploy to Vercel**

#### Option A: Deploy via Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from frontend directory
cd E:\Projects\GlobalCouponFinder\frontend
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? (your account)
# - Link to existing project? No
# - Project name: globalcouponfinder-frontend
# - Directory: ./
# - Override settings? No
```

#### Option B: Deploy via Vercel Dashboard
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import from GitHub (if you push to GitHub first)
4. Or drag and drop the `frontend` folder

### 3. **Environment Variables**

Set these in Vercel dashboard:
```
NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
NEXT_PUBLIC_ADMOB_APP_ID=ca-app-pub-9385746674842290~2532185877
NEXT_PUBLIC_ADMOB_BANNER_ID=ca-app-pub-9385746674842290/7749671776
NEXT_PUBLIC_ADMOB_INTERSTITIAL_ID=ca-app-pub-9385746674842290/2815967342
NEXT_PUBLIC_ADMOB_REWARDED_ID=ca-app-pub-9385746674842290/6615611556
```

### 4. **Build Configuration**

The project is configured with:
- **Framework**: Next.js
- **Build Command**: `npm run build`
- **Output Directory**: `.next`
- **Install Command**: `npm install`

### 5. **Features Ready for Production**

✅ **Frontend Features:**
- Homepage with hero section
- Region/Country filtering (America, Europe, Asia)
- Search functionality
- Store and coupon grids
- User authentication pages
- Premium subscription page
- Dashboard for users
- Mobile responsive design

✅ **Backend Integration:**
- API client configured
- Authentication ready
- State management with Zustand
- React Query for data fetching

✅ **Monetization:**
- AdMob integration (disabled for testing)
- Premium user features
- Free user limitations

### 6. **Testing Locally**

```bash
# Start development server
cd E:\Projects\GlobalCouponFinder\frontend
npm run dev

# Access at: http://localhost:3000
```

### 7. **Production URLs**

After deployment:
- **Frontend**: `https://globalcouponfinder-frontend.vercel.app`
- **Backend**: `https://your-backend-url.railway.app`

### 8. **Next Steps**

1. Deploy to Vercel
2. Update backend API URL in environment variables
3. Test all features
4. Enable AdMob for production
5. Set up custom domain (optional)

## 🎉 Ready for Production!

The frontend is fully functional and ready for deployment to Vercel!
