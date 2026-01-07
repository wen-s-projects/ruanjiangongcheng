import sys
import os

os.chdir(r'C:\Users\wxxoxxw\ruanjiangongcheng\backend\calorie_backend')
sys.path.insert(0, os.getcwd())

print("Current directory:", os.getcwd())
print("Python path:", sys.path[:3])

try:
    import django
    print("Django version:", django.get_version())
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')
    
    print("Starting Django server...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv, ['manage.py', 'runserver', '0.0.0.0:8000'])
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    input("Press Enter to exit...")
