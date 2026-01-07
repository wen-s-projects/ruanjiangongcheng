$anacondaPython = "C:\Users\wxxoxxw\anaconda3\python.exe"
$anacondaPip = "C:\Users\wxxoxxw\anaconda3\Scripts\pip.exe"

Write-Host "=== Step 1: Installing Dependencies ==="
& $anacondaPip install django djangorestframework djangorestframework-simplejwt pymysql python-dotenv

Write-Host "`n=== Step 2: Starting Server ==="
$server = Start-Process -FilePath $anacondaPython -ArgumentList "run_django_server.py" -NoNewWindow -PassThru
Start-Sleep -Seconds 15

Write-Host "`n=== Step 3: Testing Registration ==="
try {
    $data = '{"username":"wen","password":"211304017"}'
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $data -TimeoutSec 10
    Write-Host "✅ SUCCESS! Status: $($response.StatusCode)"
    Write-Host "Response: $($response.Content)"
} catch {
    Write-Host "❌ FAILED: $($_.Exception.Message)"
}

$server.Kill()
Write-Host "`n=== Complete ==="