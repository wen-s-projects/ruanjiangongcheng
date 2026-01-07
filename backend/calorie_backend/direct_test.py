import subprocess
import time
import socket
import sys

print("=== Direct Server Test ===")
print(f"Python version: {sys.version}")

# Check if port is available
def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('localhost', port))
        s.close()
        return True
    except:
        return False

print(f"Port 8001 in use: {check_port(8001)}")

# Start Django server
print("\nStarting Django server...")
server_process = subprocess.Popen(
    [sys.executable, "run_django_server.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,  # Combine stdout and stderr
    text=True
)

# Wait for server to start
print("Waiting 15 seconds for server to start...")
time.sleep(15)

# Check if server started
if check_port(8001):
    print("✅ Server is running on port 8001")
else:
    print("❌ Server failed to start")
    # Get output
    output = server_process.communicate(timeout=5)[0]
    print("Server output:")
    print(output)
    server_process.terminate()
    sys.exit(1)

# Test registration
print("\n=== Testing Registration ===")
try:
    import requests
    register_data = {
        "username": "wen",
        "password": "211304017"
    }
    response = requests.post(
        "http://localhost:8001/api/auth/register/",
        json=register_data,
        timeout=10
    )
    print(f"✅ Registration attempt: {response.status_code}")
    print(f"Response: {response.text}")
except ImportError:
    print("❌ requests module not installed")
except Exception as e:
    print(f"❌ Registration error: {e}")

# Cleanup
print("\nStopping server...")
server_process.terminate()
print("✅ Test complete")