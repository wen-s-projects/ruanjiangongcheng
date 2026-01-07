$anacondaPip = "C:\Users\wxxoxxw\anaconda3\Scripts\pip.exe"

Write-Host "=== Installing Missing Dependencies ==="
& $anacondaPip install python-decouple

Write-Host "`n=== Final Registration Test ==="
$anacondaPython = "C:\Users\wxxoxxw\anaconda3\python.exe"

# Start server
Write-Host "Starting Django server..."
$server = Start-Process -FilePath $anacondaPython -ArgumentList "run_django_server.py" -NoNewWindow -PassThru
Start-Sleep -Seconds 20

# Test registration for user 'wen'
Write-Host "Testing registration for user 'wen'..."
try {
    $data = '{"username":"wen","password":"211304017"}'
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $data -TimeoutSec 15
    
    if ($response.StatusCode -eq 201) {
        Write-Host "🎉 REGISTRATION SUCCESSFUL!" -ForegroundColor Green
        Write-Host "Status: $($response.StatusCode)"
        Write-Host "Response: $($response.Content)"
        Write-Host "`n✅ The registration issue has been resolved!" -ForegroundColor Cyan
    } else {
        Write-Host "⚠️ Registration returned status: $($response.StatusCode)" -ForegroundColor Yellow
        Write-Host "Response: $($response.Content)"
    }
} catch {
    Write-Host "❌ Registration failed" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)"
}

$server.Kill()
Write-Host "`n=== Test Complete ==="