import psycopg2                                                                                                                 def create_table():
    db_params = {                                                       'host': 'localhost',
        'database': 'journal',                                          'user': 'harz',
        'password': '123'                                           }                                                           
    connection = None                                                                                                               try:
        connection = psycopg2.connect(**db_params)                      cursor = connection.cursor() 

        # Create the 'users' table if it doesn't exist
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                password VARCHAR(50) NOT NULL
            );
        """
        cursor.execute(create_table_query)                      
        # Commit the changes to the database                            connection.commit()                                             print("Table 'users' created successfully!")                                                                                except psycopg2.Error as e:
        print(f"Error: Unable to create table. {e}") 

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed.") 

def add_user(username, password):
    db_params = {
        'host': 'localhost',
        'database': 'journal',
        'user': 'harz',
        'password': '123'
    } 

    connection = None 

    try:
        connection = psycopg2.connect(**db_params)
        print("Connected to the database!") 

        cursor = connection.cursor() 

        # Example: Execute SQL query to insert a user into the 'users' table
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s);"
        user_data = (username, password)
        cursor.execute(insert_query, user_data) 

        # Commit the changes to the database
        connection.commit()
        print("User added successfully!") 

    except psycopg2.Error as e:
        print(f"Error: Unable to add user to the database. {e}") 

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed.") 

# Create the 'users' table
create_table() 

# Example: Adding a user
add_user('john_doe', 'secure_password')
