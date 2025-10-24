# PATH Configuration Guide

## 🎯 **Current Status**

✅ **Python 3.11.7** - Working perfectly  
✅ **Node.js v22.20.0** - Installed but not in PATH  
✅ **Git 2.51.0** - Installed but not in PATH  

## 🔧 **Solution: Add to System PATH**

### **Method 1: Automatic (Recommended)**

1. **Right-click PowerShell** and select **"Run as Administrator"**
2. Navigate to your project:
   ```powershell
   cd E:\Projects\GlobalCouponFinder
   ```
3. Run the configuration script:
   ```powershell
   .\configure_path.ps1
   ```
4. **Restart PowerShell** or your computer

### **Method 2: Manual Configuration**

1. **Open System Properties**:
   - Press `Win + R`
   - Type `sysdm.cpl`
   - Press Enter

2. **Go to Environment Variables**:
   - Click "Advanced" tab
   - Click "Environment Variables..." button

3. **Edit System PATH**:
   - In "System variables" section
   - Find and select "Path"
   - Click "Edit..."

4. **Add These Paths**:
   - Click "New"
   - Add: `E:\node js`
   - Click "New" again
   - Add: `E:\Git\Git\bin`
   - Click "OK" on all dialogs

5. **Restart PowerShell**

## ✅ **Verification**

After configuring PATH, test with:

```powershell
# Test Node.js
node --version
# Should show: v22.20.0

# Test npm
npm --version
# Should show: 10.9.3

# Test Git
git --version
# Should show: git version 2.51.0.windows.2
```

## 🚀 **Next Steps After PATH Configuration**

1. **Install Frontend Dependencies**:
   ```powershell
   cd E:\Projects\GlobalCouponFinder\frontend
   npm install
   ```

2. **Configure npm for E: drive**:
   ```powershell
   npm config set cache E:\npm-cache
   npm config set prefix E:\npm-global
   ```

3. **Start Frontend**:
   ```powershell
   npm run dev
   ```
   Visit: http://localhost:3000

4. **Initialize Git Repository**:
   ```powershell
   cd E:\Projects\GlobalCouponFinder
   git init
   git add .
   git commit -m "Initial commit: GlobalCouponFinder setup"
   ```

## 🎉 **Complete Setup Verification**

Run the verification script:
```powershell
cd E:\Projects\GlobalCouponFinder
.\check_setup.ps1
```

**Expected Result**: All components should show ✅ (green checkmarks)

## 📊 **Current Installation Status**

| Component | Status | Location | PATH |
|-----------|--------|----------|------|
| **Python** | ✅ Working | System | ✅ |
| **Node.js** | ✅ Installed | `E:\node js\` | ❌ Needs PATH |
| **Git** | ✅ Installed | `E:\Git\Git\bin\` | ❌ Needs PATH |
| **Backend** | ✅ Ready | `E:\Projects\GlobalCouponFinder\backend\` | ✅ |
| **Frontend** | ⏳ Ready for npm | `E:\Projects\GlobalCouponFinder\frontend\` | ⏳ |

## 🎯 **Summary**

- **Python**: ✅ Perfect
- **Node.js**: ✅ Installed, needs PATH
- **Git**: ✅ Installed, needs PATH
- **Backend**: ✅ Fully working
- **Frontend**: ⏳ Ready for npm install

**Action Required**: Configure PATH for Node.js and Git, then install frontend dependencies.

**Time to Complete**: ~5 minutes
