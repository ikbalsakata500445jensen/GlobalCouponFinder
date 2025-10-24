# Configure PATH for Node.js and Git
# Run this script as Administrator to add paths to system PATH

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Configuring PATH for Node.js and Git" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

if (-not $isAdmin) {
    Write-Host "⚠️  This script needs to be run as Administrator to modify system PATH" -ForegroundColor Yellow
    Write-Host "Right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Alternatively, you can manually add these paths:" -ForegroundColor Yellow
    Write-Host "1. Open System Properties > Environment Variables" -ForegroundColor White
    Write-Host "2. Edit 'Path' in System variables" -ForegroundColor White
    Write-Host "3. Add these paths:" -ForegroundColor White
    Write-Host "   - E:\node js" -ForegroundColor Green
    Write-Host "   - E:\Git\Git\bin" -ForegroundColor Green
    Write-Host ""
    exit 1
}

# Get current system PATH
$currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")

# Paths to add
$nodePath = "E:\node js"
$gitPath = "E:\Git\Git\bin"

# Check if paths already exist
$nodeExists = $currentPath -like "*$nodePath*"
$gitExists = $currentPath -like "*$gitPath*"

Write-Host "Current PATH status:" -ForegroundColor Yellow
Write-Host "Node.js path ($nodePath): $(if($nodeExists) {'✅ Already exists'} else {'❌ Not found'})" -ForegroundColor $(if($nodeExists) {'Green'} else {'Red'})
Write-Host "Git path ($gitPath): $(if($gitExists) {'✅ Already exists'} else {'❌ Not found'})" -ForegroundColor $(if($gitExists) {'Green'} else {'Red'})
Write-Host ""

if ($nodeExists -and $gitExists) {
    Write-Host "✅ Both Node.js and Git are already in PATH!" -ForegroundColor Green
    Write-Host "You can now use 'node', 'npm', and 'git' commands from anywhere." -ForegroundColor Green
} else {
    Write-Host "Adding missing paths to system PATH..." -ForegroundColor Yellow
    
    $newPath = $currentPath
    
    if (-not $nodeExists) {
        $newPath += ";$nodePath"
        Write-Host "✅ Added Node.js path" -ForegroundColor Green
    }
    
    if (-not $gitExists) {
        $newPath += ";$gitPath"
        Write-Host "✅ Added Git path" -ForegroundColor Green
    }
    
    # Update system PATH
    [Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
    
    Write-Host ""
    Write-Host "✅ PATH updated successfully!" -ForegroundColor Green
    Write-Host "⚠️  You may need to restart PowerShell or your computer for changes to take effect." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Testing installations..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Test Node.js
try {
    $nodeVersion = & "E:\node js\node.exe" --version
    Write-Host "✅ Node.js: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js test failed" -ForegroundColor Red
}

# Test npm
try {
    $npmVersion = & "E:\node js\npm.cmd" --version
    Write-Host "✅ npm: $npmVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ npm test failed" -ForegroundColor Red
}

# Test Git
try {
    $gitVersion = & "E:\Git\Git\bin\git.exe" --version
    Write-Host "✅ Git: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git test failed" -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "1. Restart PowerShell or your computer" -ForegroundColor White
Write-Host "2. Run: .\check_setup.ps1" -ForegroundColor White
Write-Host "3. If successful, run: cd frontend && npm install" -ForegroundColor White
Write-Host "4. Then: npm run dev" -ForegroundColor White
