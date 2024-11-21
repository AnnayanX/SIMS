import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to SQLite DB successful: {db_file}")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn

def execute_query(connection, query):
    """ Execute a single query """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    """ Execute a read query and return the results """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

if __name__ == "__main__":
    # Example usage
    database = "login.db"  # Specify your database file here
    conn = create_connection(database)

    # Example to create tables
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        phone_no INTEGER,
        gender TEXT,
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        account_type TEXT NOT NULL
    );
    """
    
    execute_query(conn, create_users_table)

    # Close the connection
    if conn:
        conn.close()