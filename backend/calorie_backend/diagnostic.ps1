# Detailed diagnostic script
Write-Host "=== Detailed Diagnostic Test ===" -ForegroundColor Green

# Check if port 8001 is in use
Write-Host "Checking port 8001..."
netstat -ano | findstr :8001

# Try to start server
Write-Host "`nStarting server..."
$server = Start-Process -FilePath "python" -ArgumentList "run_django_server.py" -NoNewWindow -PassThru
Start-Sleep -Seconds 10

# Check server status
Write-Host "`nChecking server status..."
netstat -ano | findstr :8001

# Test with curl if available
Write-Host "`nTesting with curl..."
try {
    curl http://localhost:8001/
} catch {
    Write-Host "curl not available"
}

# Test registration
Write-Host "`nTesting registration..."
try {
    $data = '{"username":"wen","password":"211304017"}'
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $data -TimeoutSec 5
    Write-Host "SUCCESS: $($response.StatusCode)"
} catch {
    Write-Host "ERROR: $($_.Exception.Message)"
    Write-Host "Inner error: $($_.Exception.InnerException)"
}

# Cleanup
$server.Kill()
Write-Host "`nTest complete"