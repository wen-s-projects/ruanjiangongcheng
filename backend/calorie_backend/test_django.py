import os
import sys

os.chdir(r'C:\Users\wxxoxxw\ruanjiangongcheng\backend\calorie_backend')
sys.path.insert(0, os.getcwd())

print("Testing Django configuration...")
print("=" * 50)

try:
    import django
    print(f"✓ Django imported successfully, version: {django.get_version()}")
except ImportError as e:
    print(f"✗ Failed to import Django: {e}")
    sys.exit(1)

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')
    django.setup()
    print("✓ Django setup completed")
except Exception as e:
    print(f"✗ Django setup failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    from django.conf import settings
    print(f"✓ Settings loaded")
    print(f"  - DEBUG: {settings.DEBUG}")
    print(f"  - DATABASES: {settings.DATABASES}")
except Exception as e:
    print(f"✗ Failed to load settings: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 50)
print("All tests passed! Django is ready to run.")
print("\nTo start the server, run:")
print("  python manage.py runserver 0.0.0.0:8000")
