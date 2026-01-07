# Final test script to start server and test registration
Write-Host "=== Final Registration Test ===" -ForegroundColor Green

# Start Django server
Write-Host "Starting Django server on port 8001..."
$server = Start-Process -FilePath "python" -ArgumentList "run_django_server.py" -NoNewWindow -PassThru

# Wait for server to initialize
Write-Host "Waiting 20 seconds for server to start..."
Start-Sleep -Seconds 20

# Test registration
Write-Host "`nTesting user registration..."
try {
    $registrationData = @{
        username = "wen"
        password = "211304017"
    } | ConvertTo-Json
    
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $registrationData -TimeoutSec 15
    
    Write-Host "✅ REGISTRATION SUCCESSFUL!" -ForegroundColor Green
    Write-Host "Status Code: $($response.StatusCode)"
    Write-Host "Response: $($response.Content)"
} catch {
    Write-Host "❌ REGISTRATION FAILED" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)"
}

# Cleanup
Write-Host "`nStopping server..."
$server.Kill()
Write-Host "✅ Test complete!" -ForegroundColor Green