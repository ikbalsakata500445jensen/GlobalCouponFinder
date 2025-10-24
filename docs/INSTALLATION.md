# Installation Guide for GlobalCouponFinder

## Prerequisites

All installations must be on **E: drive** due to C: drive space limitations.

### Required Software

1. **Node.js 18+**
   - Download from: https://nodejs.org/
   - Install to: `E:\Node`
   - Add to PATH: `E:\Node` and `E:\Node\Scripts`

2. **Python 3.11+**
   - ✅ Already installed (Python 3.11.7)
   - Location: Check with `python --version`

3. **Git**
   - Download from: https://git-scm.com/
   - Install to: `E:\Git`
   - Add to PATH: `E:\Git\bin`

## Step-by-Step Installation

### 1. Configure npm for E: Drive

After installing Node.js:

```powershell
# Create npm directories on E: drive
mkdir E:\npm-cache
mkdir E:\npm-global

# Configure npm to use E: drive
npm config set cache E:\npm-cache
npm config set prefix E:\npm-global

# Add to PATH
$env:PATH += ";E:\npm-global"
```

### 2. Configure Python for E: Drive

```powershell
# Pip cache is already configured
# Verify:
pip config get global.cache-dir
# Should show: E:\pip-cache
```

### 3. Backend Setup

✅ **Already Completed**:
- Virtual environment created
- Dependencies installed
- Playwright browsers installed to E:\playwright-browsers

To activate backend:
```powershell
cd E:\Projects\GlobalCouponFinder\backend
.\venv\Scripts\Activate.ps1
python main.py
```

### 4. Frontend Setup

**After Node.js Installation**:

```powershell
cd E:\Projects\GlobalCouponFinder\frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

### 5. Initialize Git Repository

**After Git Installation**:

```powershell
cd E:\Projects\GlobalCouponFinder

# Initialize git
git init

# Add files
git add .

# First commit
git commit -m "Initial commit: GlobalCouponFinder setup"
```

## Environment Configuration

### Backend (.env)

Create `E:\Projects\GlobalCouponFinder\backend\.env`:

```env
DATABASE_URL=postgresql://user:pass@localhost:5432/couponfinder
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=change-this-to-random-string
```

### Frontend (.env.local)

Create `E:\Projects\GlobalCouponFinder\frontend\.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Verification

### Check Node.js
```powershell
node --version  # Should show v18.x.x or higher
npm --version   # Should show v9.x.x or higher
```

### Check Python
```powershell
python --version  # Should show Python 3.11.7
pip --version     # Should show pip 25.2
```

### Check Git
```powershell
git --version  # Should show git version 2.x.x
```

### Test Backend
```powershell
cd E:\Projects\GlobalCouponFinder\backend
.\venv\Scripts\Activate.ps1
python main.py
# Visit http://localhost:8000 - Should show API welcome message
```

### Test Frontend
```powershell
cd E:\Projects\GlobalCouponFinder\frontend
npm run dev
# Visit http://localhost:3000 - Should show Next.js app
```

## Troubleshooting

### Issue: Node.js not found after installation
**Solution**: Add Node.js to PATH:
1. Open System Environment Variables
2. Add `E:\Node` to System PATH
3. Add `E:\Node\Scripts` to System PATH
4. Restart PowerShell

### Issue: Git not found after installation
**Solution**: Add Git to PATH:
1. Open System Environment Variables
2. Add `E:\Git\bin` to System PATH
3. Restart PowerShell

### Issue: npm install fails with ENOSPC error
**Solution**: Clear npm cache
```powershell
npm cache clean --force
npm install
```

### Issue: Python virtual environment activation fails
**Solution**: Set execution policy
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Next Steps

After installation:

1. **Setup Free Backend Services**:
   - Create Supabase account for PostgreSQL
   - Create Upstash account for Redis
   - Create Railway account for hosting
   - Create Vercel account for frontend

2. **Configure Environment Variables**:
   - Update `.env` files with production credentials

3. **Start Development**:
   - Backend: `cd backend && .\venv\Scripts\Activate.ps1 && python main.py`
   - Frontend: `cd frontend && npm run dev`

## Important Notes

- ✅ Backend is fully configured and ready to use
- ⏳ Frontend needs Node.js installation
- ⏳ Git needs installation for version control
- 📁 All files are on E: drive as required
- 🎯 Playwright browsers are installed on E: drive
- 💾 npm and pip caches are configured for E: drive

