import psycopg2

# Database connection parameters
db_params = {
    'host': 'localhost',
    'database': 'journal',  # Updated to 'journal'
    'user': 'harz',         # Updated to 'harz'
    'password': '123'       # Updated to '123'
}

# Establish a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
    print("Connected to the database!")

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Example: Execute a SQL query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL Database Version: {db_version}")

except psycopg2.Error as e:
    print(f"Error: Unable to connect to the database. {e}")

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")

