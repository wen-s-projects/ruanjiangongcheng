$anacondaPython = "C:\Users\wxxoxxw\anaconda3\python.exe"

Write-Host "=== Final Test with Anaconda ==="

# Start server
Write-Host "Starting server..."
$server = Start-Process -FilePath $anacondaPython -ArgumentList "run_django_server.py" -NoNewWindow -PassThru
Start-Sleep -Seconds 20

# Test registration
Write-Host "Testing registration for user 'wen'..."
try {
    $data = '{"username":"wen","password":"211304017"}'
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $data -TimeoutSec 15
    
    if ($response.StatusCode -eq 201) {
        Write-Host "🎉 REGISTRATION SUCCESSFUL!" -ForegroundColor Green
        Write-Host "Status: $($response.StatusCode)"
        Write-Host "Response: $($response.Content)"
    } else {
        Write-Host "⚠️ REGISTRATION RETURNED: $($response.StatusCode)" -ForegroundColor Yellow
        Write-Host "Response: $($response.Content)"
    }
} catch {
    Write-Host "❌ REGISTRATION FAILED" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)"
    Write-Host "Inner error: $($_.Exception.InnerException)"
}

# Cleanup
$server.Kill()
Write-Host "`nTest complete"