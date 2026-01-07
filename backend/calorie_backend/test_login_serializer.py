import os
import sys
import django

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')
django.setup()

from apps.users.models import User
from apps.auth.serializers import LoginSerializer
import json

def test_login_serializer():
    """测试LoginSerializer是否正常工作"""
    print("=== 测试LoginSerializer ===")
    print()
    
    # 测试数据
    test_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    print(f"测试数据: {json.dumps(test_data, ensure_ascii=False)}")
    print()
    
    # 创建serializer实例
    serializer = LoginSerializer(data=test_data)
    
    print(f"Serializer是否有效: {serializer.is_valid()}")
    
    if not serializer.is_valid():
        print(f"验证错误: {serializer.errors}")
    else:
        print(f"验证成功!")
        print(f"用户数据: {serializer.validated_data}")
    
    print()
    print("=== 测试完成 ===")

if __name__ == "__main__":
    test_login_serializer()