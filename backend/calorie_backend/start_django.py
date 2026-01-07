import os
import sys
import subprocess

os.chdir(r'C:\Users\wxxoxxw\ruanjiangongcheng\backend\calorie_backend')

print("Starting Django server...")
print(f"Current directory: {os.getcwd()}")
print(f"Python version: {sys.version}")

try:
    result = subprocess.run(
        [sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'],
        capture_output=True,
        text=True,
        check=True
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
except subprocess.CalledProcessError as e:
    print("Error starting Django server:")
    print("STDOUT:", e.stdout)
    print("STDERR:", e.stderr)
    sys.exit(1)
