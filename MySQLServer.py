import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",      # change if using remote server
            user="root",           # change to your MySQL username
            password="@Habib0208039344", # change to your MySQL password
            database="alx_book_store" # the DB you created earlier
        )
        if connection.is_connected():
            print("Connection to MySQL successful!")
    except Error as e:
        print(f"Error: '{e}' occurred while connecting to MySQL")
    return connection

def main():
    conn = create_connection()
    if conn:
        # You can add queries here, e.g., fetch authors
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        for table in cursor.fetchall():
            print(table)
        conn.close()

if __name__ == "__main__":
    main()
