import pymysql
import os

db_name = os.getenv('DB_NAME', 'CalorieSystem')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'mysql')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '3306'))

print("=" * 80)
print("DATABASE USERS LIST")
print("=" * 80)

try:
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
    cursor.execute("SELECT id, username, is_active, is_staff, created_at FROM User ORDER BY id DESC")
    users = cursor.fetchall()
    
    print(f"\nTotal users: {len(users)}")
    print("\n" + "-" * 80)
    print(f"{'ID':<6} {'Username':<20} {'Active':<8} {'Staff':<8} {'Created At':<25}")
    print("-" * 80)
    
    for user in users:
        created_at = user['created_at'].strftime('%Y-%m-%d %H:%M:%S') if user['created_at'] else 'N/A'
        print(f"{user['id']:<6} {user['username']:<20} {user['is_active']:<8} {user['is_staff']:<8} {created_at}")
    
    print("-" * 80)
    
    connection.close()
    
except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()
