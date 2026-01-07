import pymysql
import os

db_name = os.getenv('DB_NAME', 'CalorieSystem')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'mysql')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '3306'))

print("Checking User table structure...")

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
    cursor.execute("DESCRIBE User")
    columns = cursor.fetchall()
    
    print(f"\nUser table has {len(columns)} columns:")
    for col in columns:
        print(f"  - {col['Field']}: {col['Type']} ({col['Null']}, {col['Key']}, {col['Default']})")
    
    connection.close()
    
except pymysql.Error as e:
    print(f"\n✗ MySQL Error: {e}")
except Exception as e:
    print(f"\n✗ Error: {e}")
