Write-Host "=== Testing Python Execution ==="
Write-Host "Python path: $((Get-Command python).Source)"

# Test simple Python command
Write-Host "`nTesting simple Python command:"
$output = python -c "print('Hello World'); print('Python version:', __import__('sys').version)" 2>&1
Write-Host "Output:"
Write-Host $output

# Test file execution
Write-Host "`nTesting file execution:"
$testContent = "print('Hello from file')"
Set-Content -Path test_file.py -Value $testContent
$fileOutput = python test_file.py 2>&1
Write-Host "File output:"
Write-Host $fileOutput

# Clean up
Remove-Item test_file.py -ErrorAction SilentlyContinue

Write-Host "`n=== Test Complete ==="