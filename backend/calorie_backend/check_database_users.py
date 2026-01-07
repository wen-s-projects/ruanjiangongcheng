import os
import sys
import django

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')
django.setup()

from apps.users.models import User

def check_database_users():
    """检查数据库中的用户数据"""
    print("=== 检查数据库中的用户数据 ===")
    print()
    
    # 查询所有用户
    users = User.objects.all()
    
    print(f"数据库中的用户数量: {users.count()}")
    print()
    
    # 显示每个用户的信息
    for user in users:
        print(f"用户ID: {user.id}")
        print(f"用户名: {user.username}")
        print(f"是否激活: {user.is_active}")
        print(f"是否为管理员: {user.is_staff}")
        print(f"是否为超级用户: {user.is_superuser}")
        print(f"创建时间: {user.created_at}")
        print(f"更新时间: {user.updated_at}")
        print(f"最后登录时间: {user.last_login}")
        print()
    
    # 检查是否有密码字段
    try:
        print(f"用户模型字段:")
        for field in User._meta.get_fields():
            print(f"  - {field.name}: {field.__class__.__name__}")
    except Exception as e:
        print(f"检查字段时出错: {e}")
    
    print()
    print("=== 检查完成 ===")

if __name__ == "__main__":
    check_database_users()