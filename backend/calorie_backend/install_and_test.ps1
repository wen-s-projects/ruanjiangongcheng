Write-Host "=== Installing Dependencies ==="
$anacondaPython = "C:\Users\wxxoxxw\anaconda3\python.exe"
$anacondaPip = "C:\Users\wxxoxxw\anaconda3\Scripts\pip.exe"

Write-Host "Installing Django and dependencies..."
& $anacondaPip install -r requirements.txt

Write-Host "`nStarting Django server..."
$server = Start-Process -FilePath $anacondaPython -ArgumentList "run_django_server.py" -NoNewWindow -PassThru
Start-Sleep -Seconds 20

Write-Host "`nTesting registration:"
try {
    $data = '{"username":"wen","password":"211304017"}'
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $data -TimeoutSec 15
    Write-Host "✅ REGISTRATION SUCCESSFUL!" -ForegroundColor Green
    Write-Host "Status Code: $($response.StatusCode)"
    Write-Host "Response: $($response.Content)"
} catch {
    Write-Host "❌ REGISTRATION FAILED" -ForegroundColor Red
    Write-Host "Error: $($_.Exception.Message)"
}

$server.Kill()
Write-Host "`nTest complete"