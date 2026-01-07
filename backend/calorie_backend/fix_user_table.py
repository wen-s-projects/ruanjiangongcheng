import pymysql
import os

db_name = os.getenv('DB_NAME', 'CalorieSystem')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'mysql')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '3306'))

print("Fixing User table structure...")

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
    
    # Add last_login field
    try:
        cursor.execute("ALTER TABLE User ADD COLUMN last_login DATETIME NULL DEFAULT NULL COMMENT '最后登录时间'")
        print("✓ Added last_login column")
    except pymysql.Error as e:
        if e.args[0] == 1060:
            print("✓ last_login column already exists")
        else:
            raise
    
    # Add is_superuser field
    try:
        cursor.execute("ALTER TABLE User ADD COLUMN is_superuser TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否为超级用户'")
        print("✓ Added is_superuser column")
    except pymysql.Error as e:
        if e.args[0] == 1060:
            print("✓ is_superuser column already exists")
        else:
            raise
    
    # Add is_active field
    try:
        cursor.execute("ALTER TABLE User ADD COLUMN is_active TINYINT(1) NOT NULL DEFAULT 1 COMMENT '是否激活'")
        print("✓ Added is_active column")
    except pymysql.Error as e:
        if e.args[0] == 1060:
            print("✓ is_active column already exists")
        else:
            raise
    
    # Add is_staff field
    try:
        cursor.execute("ALTER TABLE User ADD COLUMN is_staff TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否为管理员'")
        print("✓ Added is_staff column")
    except pymysql.Error as e:
        if e.args[0] == 1060:
            print("✓ is_staff column already exists")
        else:
            raise
    
    # Check if password column exists, if not rename passport to password
    try:
        cursor.execute("SHOW COLUMNS FROM User LIKE 'password'")
        result = cursor.fetchone()
        if not result:
            cursor.execute("ALTER TABLE User CHANGE COLUMN passport password VARCHAR(255) NOT NULL COMMENT '密码'")
            print("✓ Renamed passport to password")
        else:
            print("✓ password column already exists")
    except pymysql.Error as e:
        if e.args[0] == 1091:
            print("✓ password column already exists")
        else:
            raise
    
    # Add created_at field
    try:
        cursor.execute("ALTER TABLE User ADD COLUMN created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'")
        print("✓ Added created_at column")
    except pymysql.Error as e:
        if e.args[0] == 1060:
            print("✓ created_at column already exists")
        else:
            raise
    
    # Add updated_at field
    try:
        cursor.execute("ALTER TABLE User ADD COLUMN updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'")
        print("✓ Added updated_at column")
    except pymysql.Error as e:
        if e.args[0] == 1060:
            print("✓ updated_at column already exists")
        else:
            raise
    
    connection.commit()
    connection.close()
    print("\n✓ User table structure updated successfully!")
    
except pymysql.Error as e:
    print(f"\n✗ MySQL Error: {e}")
except Exception as e:
    print(f"\n✗ Error: {e}")
