import os
import sys

os.chdir(r'C:\Users\wxxoxxw\ruanjiangongcheng\backend\calorie_backend')
sys.path.insert(0, os.getcwd())

print("=" * 60)
print("Django 诊断工具")
print("=" * 60)
print()

print("1. 检查Python版本...")
print(f"   Python: {sys.version}")
print()

print("2. 检查Django安装...")
try:
    import django
    print(f"   ✓ Django已安装，版本: {django.get_version()}")
except ImportError as e:
    print(f"   ✗ Django未安装: {e}")
    sys.exit(1)
print()

print("3. 检查当前目录...")
print(f"   当前目录: {os.getcwd()}")
print()

print("4. 检查manage.py文件...")
if os.path.exists('manage.py'):
    print("   ✓ manage.py存在")
else:
    print("   ✗ manage.py不存在")
    sys.exit(1)
print()

print("5. 检查settings.py文件...")
if os.path.exists('calorie_backend/settings.py'):
    print("   ✓ settings.py存在")
else:
    print("   ✗ settings.py不存在")
    sys.exit(1)
print()

print("6. 加载Django设置...")
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')
    django.setup()
    print("   ✓ Django设置加载成功")
except Exception as e:
    print(f"   ✗ Django设置加载失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
print()

print("7. 检查数据库配置...")
try:
    from django.conf import settings
    print(f"   ✓ 数据库引擎: {settings.DATABASES['default']['ENGINE']}")
    print(f"   ✓ 数据库名称: {settings.DATABASES['default']['NAME']}")
except Exception as e:
    print(f"   ✗ 数据库配置检查失败: {e}")
    sys.exit(1)
print()

print("8. 检查应用...")
try:
    from django.apps import apps
    print("   ✓ 已安装的应用:")
    for app in apps.get_app_configs():
        print(f"      - {app.name}")
except Exception as e:
    print(f"   ✗ 应用检查失败: {e}")
    sys.exit(1)
print()

print("=" * 60)
print("所有检查通过！Django配置正常。")
print("=" * 60)
print()
print("现在可以启动Django服务器:")
print("  python manage.py runserver 0.0.0.0:8000")
print()
input("按Enter键退出...")
