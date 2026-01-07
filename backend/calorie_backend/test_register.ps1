# Simple test script
Write-Host "=== Starting Django Server ==="
$serverProcess = Start-Process -FilePath "python" -ArgumentList "run_django_server.py" -NoNewWindow -PassThru
Start-Sleep -Seconds 15

Write-Host "=== Testing Registration ==="
try {
    $data = '{"username":"testuser","password":"testpassword123"}'
    $response = Invoke-WebRequest -Uri "http://localhost:8001/api/auth/register/" -Method POST -Headers @{"Content-Type"="application/json"} -Body $data -TimeoutSec 10
    Write-Host "SUCCESS! Status: $($response.StatusCode)"
    Write-Host "Response: $($response.Content)"
} catch {
    Write-Host "FAILED: $($_.Exception.Message)"
}

$serverProcess.Kill()
Write-Host "=== Test Complete ==="