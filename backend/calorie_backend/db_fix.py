import pymysql

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql',
    'database': 'CalorieSystem',
    'charset': 'utf8mb4'
}

print("=== Database Fix Script ===")

try:
    # Connect to MySQL
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    print("✓ Connected to MySQL database")
    
    # List of columns to add
    columns_to_add = [
        ("last_login", "DATETIME NULL DEFAULT NULL"),
        ("is_superuser", "TINYINT(1) NOT NULL DEFAULT 0"),
        ("is_active", "TINYINT(1) NOT NULL DEFAULT 1"),
        ("is_staff", "TINYINT(1) NOT NULL DEFAULT 0"),
        ("created_at", "DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP"),
        ("updated_at", "DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    ]
    
    # Add each column
    for col_name, col_def in columns_to_add:
        try:
            cursor.execute(f"ALTER TABLE User ADD COLUMN {col_name} {col_def}")
            print(f"✓ Added {col_name}")
        except pymysql.Error as e:
            if e.args[0] == 1060:
                print(f"✓ {col_name} already exists")
            else:
                print(f"⚠️ Error adding {col_name}: {e}")
    
    # Rename passport to password if needed
    try:
        cursor.execute("SHOW COLUMNS FROM User LIKE 'password'")
        if not cursor.fetchone():
            try:
                cursor.execute("ALTER TABLE User CHANGE COLUMN passport password VARCHAR(255) NOT NULL")
                print("✓ Renamed passport to password")
            except pymysql.Error as e:
                print(f"⚠️ Error renaming column: {e}")
        else:
            print("✓ password column already exists")
    except pymysql.Error as e:
        print(f"⚠️ Error checking password column: {e}")
    
    # Commit changes
    conn.commit()
    print("\n✓ All database changes committed!")
    
    # Show final table structure
    print("\n=== Final User Table Structure ===")
    cursor.execute("DESCRIBE User")
    for row in cursor.fetchall():
        print(f"{row[0]:<20} {row[1]:<40} {row[2]:<10} {row[3]:<10} {row[4] if row[4] else 'NULL':<10}")
    
    conn.close()
    print("\n✅ Database fix completed successfully!")
    
except pymysql.Error as e:
    print(f"\n❌ MySQL Error: {e}")
except Exception as e:
    print(f"\n❌ Error: {e}")

print("\n=== Next Steps ===")
print("1. Run 'python run_django_server.py' to start the backend")
print("2. Test registration at http://localhost:8000/api/auth/register/")