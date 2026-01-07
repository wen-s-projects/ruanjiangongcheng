import sys
import os

print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Current directory:", os.getcwd())
print("Python path:", sys.path)

try:
    import django
    print("Django version:", django.VERSION)
except ImportError as e:
    print("Django import error:", e)

try:
    from decouple import config
    print("python-decouple imported successfully")
except ImportError as e:
    print("python-decouple import error:", e)

try:
    import pymysql
    print("pymysql version:", pymysql.__version__)
except ImportError as e:
    print("pymysql import error:", e)

try:
    import bcrypt
    print("bcrypt version:", bcrypt.__version__)
except ImportError as e:
    print("bcrypt import error:", e)

print("\nEnvironment variables:")
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))
