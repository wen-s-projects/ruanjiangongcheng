import requests
import json
import pymysql
import os

db_name = os.getenv('DB_NAME', 'CalorieSystem')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'mysql')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '3306'))

print("=" * 50)
print("Step 1: Registering a new user...")
print("=" * 50)

url = "http://localhost:8000/api/auth/register/"
data = {
    "username": "demo_user_2024",
    "password": "demo123456",
    "email": "demo@example.com"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    
    if response.status_code == 201:
        print("\n" + "=" * 50)
        print("Step 2: Querying database for users...")
        print("=" * 50)
        
        connection = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        
        cursor = connection.cursor()
        
        # Query all users
        cursor.execute("SELECT id, username, is_active, is_staff, created_at FROM User ORDER BY id DESC LIMIT 10")
        users = cursor.fetchall()
        
        print(f"\nTotal users in database: {len(users)}")
        print("\nRecent users:")
        print("-" * 80)
        print(f"{'ID':<5} {'Username':<20} {'Active':<8} {'Staff':<8} {'Created At':<20}")
        print("-" * 80)
        
        for user in users:
            print(f"{user['id']:<5} {user['username']:<20} {user['is_active']:<8} {user['is_staff']:<8} {user['created_at']}")
        
        print("-" * 80)
        
        # Query the newly created user
        cursor.execute("SELECT * FROM User WHERE username = %s", (data['username'],))
        new_user = cursor.fetchone()
        
        if new_user:
            print(f"\nNewly created user details:")
            print("-" * 80)
            for key, value in new_user.items():
                print(f"{key:<20} {value}")
            print("-" * 80)
        
        connection.close()
        
except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()
