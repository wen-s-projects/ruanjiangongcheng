import os
import sys
import django

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')
django.setup()

from apps.users.models import User
from apps.auth.serializers import LoginSerializer

def test_login_step_by_step():
    """逐步测试登录流程"""
    print("=== 逐步测试登录流程 ===")
    print()
    
    # 步骤1: 查询用户
    print("步骤1: 查询用户")
    try:
        user = User.objects.get(username="wen")
        print(f"   用户ID: {user.id}")
        print(f"   用户名: {user.username}")
        print(f"   是否激活: {user.is_active}")
        print(f"   密码哈希: {user.password[:20]}...")
        print()
    except User.DoesNotExist:
        print("   ❌ 用户不存在!")
        return
    
    # 步骤2: 测试密码验证
    print("步骤2: 测试密码验证")
    if user.check_password("211304017"):
        print("   ✅ 密码验证成功!")
    else:
        print("   ❌ 密码验证失败!")
        return
    
    # 步骤3: 测试序列化器
    print("步骤3: 测试序列化器")
    login_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    serializer = LoginSerializer(data=login_data)
    print(f"   序列化器是否有效: {serializer.is_valid()}")
    
    if serializer.is_valid():
        print("   ✅ 序列化器验证成功!")
        print(f"   用户数据: {serializer.validated_data}")
    else:
        print("   ❌ 序列化器验证失败!")
        print(f"   错误信息: {serializer.errors}")
        return
    
    # 步骤4: 测试令牌生成
    print("步骤4: 测试令牌生成")
    try:
        from apps.auth.views import generate_tokens
        tokens = generate_tokens(user)
        print(f"   Access Token: {tokens['access_token'][:20]}...")
        print(f"   Refresh Token: {tokens['refresh_token'][:20]}...")
        print("   ✅ 令牌生成成功!")
    except Exception as e:
        print(f"   ❌ 令牌生成失败: {e}")
        return
    
    print()
    print("=== 测试完成 ===")

if __name__ == "__main__":
    test_login_step_by_step()