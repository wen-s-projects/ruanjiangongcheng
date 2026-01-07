import subprocess
import sys
import os

os.chdir(r'C:\Users\wxxoxxw\ruanjiangongcheng\backend\calorie_backend')

print("Starting Django server on http://0.0.0.0:8000")
print("Press Ctrl+C to stop the server")
print("-" * 50)

subprocess.run([sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'])
