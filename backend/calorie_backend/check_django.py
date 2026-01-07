import os
import sys

print("=== Django Configuration Check ===")
print(f"Python: {sys.version}")
print(f"Current directory: {os.getcwd()}")

# Check if Django is installed
try:
    import django
    print(f"Django version: {django.__version__}")
except ImportError:
    print("❌ Django not installed")
    sys.exit(1)

# Check settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')

# Try to import settings
try:
    from django.conf import settings
    print("✅ Settings imported successfully")
    print(f"DEBUG: {settings.DEBUG}")
    print(f"SECRET_KEY: Set" if settings.SECRET_KEY else "❌ SECRET_KEY not set")
    print(f"DATABASES: {settings.DATABASES.keys()}")
except Exception as e:
    print(f"❌ Error importing settings: {e}")
    sys.exit(1)

# Check if manage.py exists
if os.path.exists('manage.py'):
    print("✅ manage.py exists")
else:
    print("❌ manage.py not found")

print("=== Check Complete ===")