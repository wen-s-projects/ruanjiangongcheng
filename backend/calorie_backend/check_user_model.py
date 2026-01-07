import os
import sys
import django

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 初始化Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')
django.setup()

from apps.users.models import User

def check_user_table_structure():
    """检查User表结构"""
    print("=== 检查User表结构 ===")
    
    # 获取User模型的所有字段
    fields = User._meta.get_fields()
    
    print("User表字段列表:")
    for field in fields:
        print(f"  - {field.name}: {field.__class__.__name__}")
    
    print()
    
    # 检查是否有is_superuser字段
    has_is_superuser = any(field.name == 'is_superuser' for field in fields)
    
    if has_is_superuser:
        print("✅ User表包含is_superuser字段")
    else:
        print("❌ User表缺少is_superuser字段")
        print("   这可能导致登录时出现500错误")
    
    print()
    
    # 尝试查询一个用户
    try:
        user = User.objects.first()
        if user:
            print(f"✅ 成功查询到用户: {user.username}")
            print(f"   用户ID: {user.id}")
            print(f"   是否激活: {user.is_active}")
            print(f"   是否为管理员: {user.is_staff}")
            
            # 尝试访问is_superuser属性
            try:
                is_superuser = user.is_superuser
                print(f"   是否为超级用户: {is_superuser}")
            except AttributeError as e:
                print(f"   ❌ 访问is_superuser时出错: {e}")
        else:
            print("⚠️  数据库中没有用户")
    except Exception as e:
        print(f"❌ 查询用户时出错: {e}")

if __name__ == "__main__":
    check_user_table_structure()