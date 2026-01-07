import os
import pymysql

db_name = os.getenv('DB_NAME', 'CalorieSystem')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'mysql')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '3306'))

print(f"Attempting to connect to MySQL database...")
print(f"Host: {db_host}")
print(f"Port: {db_port}")
print(f"User: {db_user}")
print(f"Database: {db_name}")

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
    print("\n✓ Successfully connected to MySQL database!")
    
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print(f"\nTables in database ({len(tables)}):")
    for table in tables:
        print(f"  - {list(table.values())[0]}")
    
    connection.close()
    print("\n✓ Database connection test completed successfully!")
    
except pymysql.Error as e:
    print(f"\n✗ MySQL Error: {e}")
    print("\nPossible solutions:")
    print("1. Make sure MySQL server is running")
    print("2. Check if the database 'CalorieSystem' exists")
    print("3. Verify the username and password are correct")
    print("4. Check if MySQL is listening on the correct port")
except Exception as e:
    print(f"\n✗ Error: {e}")
