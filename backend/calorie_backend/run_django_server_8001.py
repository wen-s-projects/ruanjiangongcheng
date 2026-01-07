import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')

try:
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8001'])
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc
