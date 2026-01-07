import pymysql
import os
import subprocess
import time

db_name = os.getenv('DB_NAME', 'CalorieSystem')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'mysql')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '3306'))

print("=== Comprehensive User Table Fix ===")

# Fix database structure
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
    
    # List of all required columns and their definitions
    required_columns = [
        ('last_login', "DATETIME NULL DEFAULT NULL COMMENT '最后登录时间'"),
        ('is_superuser', "TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否为超级用户'"),
        ('is_active', "TINYINT(1) NOT NULL DEFAULT 1 COMMENT '是否激活'"),
        ('is_staff', "TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否为管理员'"),
        ('created_at', "DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'"),
        ('updated_at', "DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'")
    ]
    
    # Add each column if missing
    for column_name, column_def in required_columns:
        try:
            cursor.execute(f"ALTER TABLE User ADD COLUMN {column_name} {column_def}")
            print(f"✓ Added {column_name} column")
        except pymysql.Error as e:
            if e.args[0] == 1060:
                print(f"✓ {column_name} column already exists")
            else:
                print(f"⚠️ Error adding {column_name}: {e}")
    
    # Check and rename passport to password if needed
    try:
        cursor.execute("SHOW COLUMNS FROM User LIKE 'password'")
        result = cursor.fetchone()
        if not result:
            try:
                cursor.execute("ALTER TABLE User CHANGE COLUMN passport password VARCHAR(255) NOT NULL COMMENT '密码'")
                print("✓ Renamed passport to password")
            except pymysql.Error as e:
                if e.args[0] == 1091:
                    print("⚠️ Column passport does not exist")
                else:
                    print(f"⚠️ Error renaming column: {e}")
        else:
            print("✓ password column already exists")
    except pymysql.Error as e:
        print(f"⚠️ Error checking password column: {e}")
    
    connection.commit()
    connection.close()
    print("\n✓ Database structure fix completed!")
    
except pymysql.Error as e:
    print(f"\n✗ MySQL Error: {e}")
except Exception as e:
    print(f"\n✗ Error: {e}")

# Start Django server
print("\n=== Starting Django Server ===")
print("Starting server on port 8000...")

# Run Django server in background
process = subprocess.Popen(
    ['python', 'run_django_server.py'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Wait for server to start
time.sleep(5)

# Check if server is running
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('localhost', 8000))
    print("✓ Django server is running on port 8000")
    s.close()
except:
    print("✗ Django server failed to start")
    # Get error output
    stdout, stderr = process.communicate(timeout=5)
    print("Server error output:")
    print(stderr)

print("\n=== Fix Process Complete ===")
print("You can now test the registration functionality at:")
print("http://localhost:8000/api/auth/register/")