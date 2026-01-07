import subprocess
import time
import sys

print(f"Python executable: {sys.executable}")
print(f"Current directory: {subprocess.getcwd()}")

# Try to run Django server with detailed error capturing
print("\n=== Starting Django Server ===")
print("Running: python run_django_server.py")

# Start server process
process = subprocess.Popen(
    [sys.executable, "run_django_server.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    cwd=r"c:\Users\wxxoxxw\ruanjiangongcheng\backend\calorie_backend"
)

# Wait a bit for output
time.sleep(3)

# Get output
stdout, stderr = process.communicate(timeout=10)

print("\n=== Server Output ===")
print("STDOUT:")
print(stdout)
print("\nSTDERR:")
print(stderr)
print(f"\nReturn code: {process.returncode}")

print("\n=== Debug Information ===")
# Check if manage.py exists
import os
manage_py_path = r"c:\Users\wxxoxxw\ruanjiangongcheng\backend\calorie_backend\manage.py"
if os.path.exists(manage_py_path):
    print(f"manage.py exists: {manage_py_path}")
else:
    print(f"manage.py NOT found: {manage_py_path}")

# Check directory structure
print("\nDirectory contents:")
for item in os.listdir(r"c:\Users\wxxoxxw\ruanjiangongcheng\backend\calorie_backend"):
    print(f"  - {item}")