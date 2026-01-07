# Debug script for Django server
Write-Host "=== Debug Script ===" -ForegroundColor Green

# Check Python environment
Write-Host "Python version:"
python --version

Write-Host "`nCurrent directory:"
Get-Location

Write-Host "`nFiles in current directory:"
Get-ChildItem

# Try to run Django server
Write-Host "`n=== Starting Django Server ===" -ForegroundColor Green
$serverProcess = Start-Process -FilePath "python" -ArgumentList "run_django_server.py" -NoNewWindow -PassThru

# Wait for server to start
Write-Host "Waiting for server to start..."
Start-Sleep -Seconds 10

# Test server connectivity
Write-Host "`n=== Testing Server Connectivity ===" -ForegroundColor Green
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8001/" -TimeoutSec 5
    Write-Host "Server is running! Status code: $($response.StatusCode)"
    Write-Host "Response: $($response.Content)"
} catch {
    Write-Host "Error connecting to server: $($_.Exception.Message)"
}

# Test registration API
Write-Host "`n=== Testing Registration API ===" -ForegroundColor Green
try {
    $registerData = @{
        username = "testuser"
        password = "testpassword123"
    } | ConvertTo-Json
    
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $registerData -TimeoutSec 10
    Write-Host "Registration test: SUCCESS!" -ForegroundColor Green
    Write-Host "Status code: $($response.StatusCode)"
    Write-Host "Response: $($response.Content)"
} catch {
    Write-Host "Registration test: FAILED" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)"
}

# Cleanup
Write-Host "`n=== Cleaning Up ===" -ForegroundColor Green
try {
    $serverProcess.Kill()
    Write-Host "Server process killed"
} catch {
    Write-Host "Error killing server process: $($_.Exception.Message)"
}

Write-Host "`n=== Debug Complete ===" -ForegroundColor Green