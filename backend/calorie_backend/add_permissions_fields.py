import pymysql
import os

db_name = os.getenv('DB_NAME', 'CalorieSystem')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'mysql')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '3306'))

print("Adding required fields to User table...")

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
    
    # Check and add is_superuser field
    cursor.execute("SHOW COLUMNS FROM User LIKE 'is_superuser'")
    result = cursor.fetchone()
    
    if result:
        print("✓ is_superuser column already exists")
    else:
        cursor.execute("ALTER TABLE User ADD COLUMN is_superuser TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否为超级管理员'")
        print("✓ Successfully added is_superuser column to User table")
    
    # Check and add groups field (many-to-many relationship)
    cursor.execute("SHOW TABLES LIKE 'User_groups'")
    result = cursor.fetchone()
    
    if result:
        print("✓ User_groups table already exists")
    else:
        cursor.execute("""
            CREATE TABLE User_groups (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                group_id INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
                UNIQUE KEY user_group (user_id, group_id)
            )
        """)
        print("✓ Successfully created User_groups table")
    
    # Check and add user_permissions field (many-to-many relationship)
    cursor.execute("SHOW TABLES LIKE 'User_user_permissions'")
    result = cursor.fetchone()
    
    if result:
        print("✓ User_user_permissions table already exists")
    else:
        cursor.execute("""
            CREATE TABLE User_user_permissions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                permission_id INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
                UNIQUE KEY user_permission (user_id, permission_id)
            )
        """)
        print("✓ Successfully created User_user_permissions table")
    
    connection.commit()
    connection.close()
    print("\n✓ Database update completed successfully!")
    
except pymysql.Error as e:
    print(f"\n✗ MySQL Error: {e}")
except Exception as e:
    print(f"\n✗ Error: {e}")
