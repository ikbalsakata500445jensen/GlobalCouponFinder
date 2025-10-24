# Start Backend Server Script
# This script activates the virtual environment and starts the FastAPI backend

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GlobalCouponFinder - Backend Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to backend directory
Set-Location -Path "E:\Projects\GlobalCouponFinder\backend"

# Check if virtual environment exists
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    Write-Host "✓ Virtual environment found" -ForegroundColor Green
    
    # Activate virtual environment
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & ".\venv\Scripts\Activate.ps1"
    
    # Check if main.py exists
    if (Test-Path ".\main.py") {
        Write-Host "✓ main.py found" -ForegroundColor Green
        Write-Host ""
        Write-Host "Starting FastAPI server..." -ForegroundColor Yellow
        Write-Host "Server will be available at: http://localhost:8000" -ForegroundColor Cyan
        Write-Host "API docs will be available at: http://localhost:8000/docs" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
        Write-Host ""
        
        # Start the server
        python main.py
    }
    else {
        Write-Host "✗ main.py not found!" -ForegroundColor Red
        Write-Host "Please ensure you're in the correct directory." -ForegroundColor Red
    }
}
else {
    Write-Host "✗ Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run setup first." -ForegroundColor Red
}

