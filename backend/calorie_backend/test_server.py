import subprocess
import time
import requests

print("=== Starting Backend Server ===")

# Start Django server
server_process = subprocess.Popen(
    ['python', 'run_django_server.py'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

print("Server starting...")
time.sleep(10)  # Wait for server to fully start

# Test if server is running
print("\n=== Testing Server Status ===")
try:
    response = requests.get('http://localhost:8000/')
    print(f"Server response: {response.status_code}")
    print(f"Server message: {response.text}")
except Exception as e:
    print(f"Server not reachable: {e}")
    # Get server error output
    stdout, stderr = server_process.communicate(timeout=5)
    print("Server stderr:", stderr)

print("\n=== Testing Registration API ===")
try:
    register_data = {
        "username": "testuser",
        "password": "testpassword123"
    }
    response = requests.post('http://localhost:8000/api/auth/register/', json=register_data)
    print(f"Registration response: {response.status_code}")
    print(f"Registration content: {response.text}")
except Exception as e:
    print(f"Registration test failed: {e}")

print("\n=== Test Complete ===")