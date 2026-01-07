import subprocess
import time
import requests

print("=== Starting Backend Server ===")

# Start Django server
server = subprocess.Popen(
    ["python", "run_django_server.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

print("Server starting...")
time.sleep(20)  # Give server more time to start

# Test server
print("\n=== Testing Server ===")
try:
    # Test root endpoint
    root_response = requests.get("http://localhost:8001/", timeout=5)
    print(f"Root endpoint: {root_response.status_code}")
    print(f"Root response: {root_response.text}")
    
    # Test registration
    print("\n=== Testing Registration ===")
    register_data = {
        "username": "testuser",
        "password": "testpassword123"
    }
    reg_response = requests.post(
        "http://localhost:8001/api/auth/register/",
        json=register_data,
        timeout=10
    )
    print(f"Registration: {reg_response.status_code}")
    print(f"Registration response: {reg_response.text}")
    
except Exception as e:
    print(f"Error: {e}")
    # Get server error output
    stdout, stderr = server.communicate()
    print("Server stdout:", stdout)
    print("Server stderr:", stderr)

# Cleanup
server.terminate()
print("\n=== Test Complete ===")