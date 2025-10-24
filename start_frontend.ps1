# Start Frontend Server Script
# This script starts the Next.js frontend development server

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GlobalCouponFinder - Frontend Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to frontend directory
Set-Location -Path "E:\Projects\GlobalCouponFinder\frontend"

# Check if Node.js is installed
$nodeVersion = node --version 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Node.js installed: $nodeVersion" -ForegroundColor Green
    
    # Check if node_modules exists
    if (Test-Path ".\node_modules") {
        Write-Host "✓ Dependencies installed" -ForegroundColor Green
    }
    else {
        Write-Host "✗ Dependencies not installed" -ForegroundColor Yellow
        Write-Host "Installing dependencies..." -ForegroundColor Yellow
        npm install
    }
    
    # Check if package.json exists
    if (Test-Path ".\package.json") {
        Write-Host "✓ package.json found" -ForegroundColor Green
        Write-Host ""
        Write-Host "Starting Next.js development server..." -ForegroundColor Yellow
        Write-Host "Server will be available at: http://localhost:3000" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
        Write-Host ""
        
        # Start the server
        npm run dev
    }
    else {
        Write-Host "✗ package.json not found!" -ForegroundColor Red
        Write-Host "Please ensure you're in the correct directory." -ForegroundColor Red
    }
}
else {
    Write-Host "✗ Node.js is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Node.js to E:\Node" -ForegroundColor Yellow
    Write-Host "Download from: https://nodejs.org/" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "After installation, configure npm:" -ForegroundColor Yellow
    Write-Host "  npm config set cache E:\npm-cache" -ForegroundColor Cyan
    Write-Host "  npm config set prefix E:\npm-global" -ForegroundColor Cyan
}

