# Setup Verification Script
# This script checks the setup status of GlobalCouponFinder

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GlobalCouponFinder - Setup Verification" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$allGood = $true

# Check Python
Write-Host "Checking Python..." -ForegroundColor Yellow
$pythonVersion = python --version 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Python installed: $pythonVersion" -ForegroundColor Green
}
else {
    Write-Host "✗ Python not found!" -ForegroundColor Red
    $allGood = $false
}

# Check pip
$pipVersion = pip --version 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ pip installed: $pipVersion" -ForegroundColor Green
}
else {
    Write-Host "✗ pip not found!" -ForegroundColor Red
    $allGood = $false
}

Write-Host ""

# Check Node.js
Write-Host "Checking Node.js..." -ForegroundColor Yellow
$nodeVersion = node --version 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Node.js installed: $nodeVersion" -ForegroundColor Green
}
else {
    Write-Host "✗ Node.js not installed" -ForegroundColor Red
    Write-Host "  Download from: https://nodejs.org/" -ForegroundColor Cyan
    $allGood = $false
}

# Check npm
$npmVersion = npm --version 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ npm installed: $npmVersion" -ForegroundColor Green
}
else {
    Write-Host "✗ npm not found!" -ForegroundColor Red
    $allGood = $false
}

Write-Host ""

# Check Git
Write-Host "Checking Git..." -ForegroundColor Yellow
$gitVersion = git --version 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Git installed: $gitVersion" -ForegroundColor Green
}
else {
    Write-Host "✗ Git not installed" -ForegroundColor Red
    Write-Host "  Download from: https://git-scm.com/" -ForegroundColor Cyan
    $allGood = $false
}

Write-Host ""

# Check Backend
Write-Host "Checking Backend..." -ForegroundColor Yellow
if (Test-Path "E:\Projects\GlobalCouponFinder\backend\venv") {
    Write-Host "✓ Backend virtual environment exists" -ForegroundColor Green
}
else {
    Write-Host "✗ Backend virtual environment not found!" -ForegroundColor Red
    $allGood = $false
}

if (Test-Path "E:\Projects\GlobalCouponFinder\backend\main.py") {
    Write-Host "✓ Backend main.py exists" -ForegroundColor Green
}
else {
    Write-Host "✗ Backend main.py not found!" -ForegroundColor Red
    $allGood = $false
}

if (Test-Path "E:\Projects\GlobalCouponFinder\backend\requirements.txt") {
    Write-Host "✓ Backend requirements.txt exists" -ForegroundColor Green
}
else {
    Write-Host "✗ Backend requirements.txt not found!" -ForegroundColor Red
    $allGood = $false
}

Write-Host ""

# Check Frontend
Write-Host "Checking Frontend..." -ForegroundColor Yellow
if (Test-Path "E:\Projects\GlobalCouponFinder\frontend\package.json") {
    Write-Host "✓ Frontend package.json exists" -ForegroundColor Green
}
else {
    Write-Host "✗ Frontend package.json not found!" -ForegroundColor Red
    $allGood = $false
}

if (Test-Path "E:\Projects\GlobalCouponFinder\frontend\node_modules") {
    Write-Host "✓ Frontend dependencies installed" -ForegroundColor Green
}
else {
    Write-Host "⚠ Frontend dependencies not installed" -ForegroundColor Yellow
    Write-Host "  Run: cd frontend && npm install" -ForegroundColor Cyan
}

Write-Host ""

# Check Playwright
Write-Host "Checking Playwright..." -ForegroundColor Yellow
if (Test-Path "E:\playwright-browsers") {
    Write-Host "✓ Playwright browsers directory exists" -ForegroundColor Green
}
else {
    Write-Host "✗ Playwright browsers not found!" -ForegroundColor Red
    $allGood = $false
}

Write-Host ""

# Check pip cache
Write-Host "Checking E: Drive Configuration..." -ForegroundColor Yellow
if (Test-Path "E:\pip-cache") {
    Write-Host "✓ pip cache directory exists" -ForegroundColor Green
}
else {
    Write-Host "⚠ pip cache directory not found" -ForegroundColor Yellow
}

if (Test-Path "E:\npm-cache") {
    Write-Host "✓ npm cache directory exists" -ForegroundColor Green
}
elseif ($nodeVersion) {
    Write-Host "⚠ npm cache directory not found" -ForegroundColor Yellow
    Write-Host "  Run: npm config set cache E:\npm-cache" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan

if ($allGood) {
    Write-Host "✓ All critical components are installed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "You can start the servers:" -ForegroundColor Cyan
    Write-Host "  Backend:  .\start_backend.ps1" -ForegroundColor White
    Write-Host "  Frontend: .\start_frontend.ps1" -ForegroundColor White
}
else {
    Write-Host "✗ Some components are missing!" -ForegroundColor Red
    Write-Host "Please check the messages above." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "For detailed setup instructions, see:" -ForegroundColor Cyan
    Write-Host "  SETUP_STATUS.md" -ForegroundColor White
    Write-Host "  docs\INSTALLATION.md" -ForegroundColor White
}

Write-Host "========================================" -ForegroundColor Cyan

