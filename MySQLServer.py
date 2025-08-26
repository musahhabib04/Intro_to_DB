import mysql.connector
from mysql.connector import Error

def create_server_connection():
    """Connect to MySQL server (no database yet)."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # change to your MySQL username
            password="@Habib0208039344"  # change to your MySQL password
        )
        if connection.is_connected():
            print("✅ Connection to MySQL server successful!")
    except mysql.connector.Error as err:   # <-- explicit exception handling
        print(f"❌ Error: '{err}' occurred while connecting to MySQL server")
    return connection

def create_database(connection, query):
    """Create a database if it does not exist."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("✅ Database created successfully (or already exists).")
    except Error as e:
        print(f"❌ Error: '{e}' occurred while creating database")

def main():
    server_conn = create_server_connection()
    if server_conn:
        create_database(server_conn, "CREATE DATABASE IF NOT EXISTS alx_book_store;")
        server_conn.close()

if __name__ == "__main__":
    main()
