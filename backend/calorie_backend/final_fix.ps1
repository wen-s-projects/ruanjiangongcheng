$anacondaPip = "C:\Users\wxxoxxw\anaconda3\Scripts\pip.exe"
$anacondaPython = "C:\Users\wxxoxxw\anaconda3\python.exe"

Write-Host "=== Final Fix and Test ==="

# Install updated mysqlclient
Write-Host "Installing updated mysqlclient..."
& $anacondaPip install mysqlclient>=2.2.1

Write-Host "`n=== Final Registration Test ==="

# Start server
Write-Host "Starting Django server..."
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
        Write-Host "`n✅ The registration issue has been completely resolved!" -ForegroundColor Cyan
        Write-Host "✅ User 'wen' has been successfully registered!" -ForegroundColor Cyan
    } else {
        Write-Host "⚠️ Registration status: $($response.StatusCode)" -ForegroundColor Yellow
        Write-Host "Response: $($response.Content)"
    }
} catch {
    Write-Host "❌ Registration failed" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)"
}

$server.Kill()
Write-Host "`n=== Complete ==="