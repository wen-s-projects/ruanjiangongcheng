import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')

print("Testing Django configuration...")
print(f"Current directory: {os.getcwd()}")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

try:
    import django
    print(f"Django version: {django.VERSION}")
    django.setup()
    print("Django setup successful!")
    
    from django.conf import settings
    print(f"DEBUG: {settings.DEBUG}")
    print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"DATABASES: {settings.DATABASES}")
    print(f"AUTH_USER_MODEL: {settings.AUTH_USER_MODEL}")
    
    from django.core.management import call_command
    print("\nRunning system check...")
    call_command('check', verbosity=2)
    
    print("\n✓ Django configuration is valid!")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
