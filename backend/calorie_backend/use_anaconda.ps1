Write-Host "=== Using Anaconda Python ==="
$anacondaPython = "C:\Users\wxxoxxw\anaconda3\python.exe"

Write-Host "Python version:"
& $anacondaPython --version

Write-Host "`nTesting Django server:"
$server = Start-Process -FilePath $anacondaPython -ArgumentList "run_django_server.py" -NoNewWindow -PassThru
Start-Sleep -Seconds 15

Write-Host "`nTesting registration:"
try {
    $data = '{"username":"wen","password":"211304017"}'
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $data -TimeoutSec 10
    Write-Host "✅ SUCCESS! Status: $($response.StatusCode)"
    Write-Host "Response: $($response.Content)"
} catch {
    Write-Host "❌ FAILED: $($_.Exception.Message)"
}

$server.Kill()
Write-Host "`nTest complete"