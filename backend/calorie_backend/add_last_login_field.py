import pymysql
import os

db_name = os.getenv('DB_NAME', 'CalorieSystem')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'mysql')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '3306'))

print("Adding last_login field to User table...")

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
    
    # Check if last_login column exists
    cursor.execute("SHOW COLUMNS FROM User LIKE 'last_login'")
    result = cursor.fetchone()
    
    if result:
        print("✓ last_login column already exists")
    else:
        # Add last_login column
        cursor.execute("ALTER TABLE User ADD COLUMN last_login DATETIME NULL COMMENT '最后登录时间'")
        print("✓ Successfully added last_login column to User table")
    
    connection.commit()
    connection.close()
    print("\n✓ Database update completed successfully!")
    
except pymysql.Error as e:
    print(f"\n✗ MySQL Error: {e}")
except Exception as e:
    print(f"\n✗ Error: {e}")
