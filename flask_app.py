# flask_app.py
from flask import Flask, render_template, jsonify, request
from flask_bcrypt import Bcrypt
import psycopg2
from psycopg2 import sql

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Update these with your PostgreSQL connection details
db_params = {
    'host': 'localhost',
    'database': 'journal',  # Change to your database name
    'user': 'harz',         # Change to your PostgreSQL username
    'password': '123'       # Change to your PostgreSQL password
}

def create_user_table():
    # Create the 'users' table if it doesn't exist
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username VARCHAR(50) PRIMARY KEY,
                    password VARCHAR(50) NOT NULL
                );
            """)

create_user_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        new_user = request.json
        new_user['password'] = bcrypt.generate_password_hash(new_user['password']).decode('utf-8')
        insert_user(new_user)
        return jsonify(new_user), 201
    elif request.method == 'GET':
        users_data = select_all_users()
        for user in users_data:
            user['password'] = '********'  # Replace with some secure placeholder
        return jsonify(users_data)

def insert_user(user):
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (username, password)
                VALUES (%s, %s);
            """, (user['username'], user['password']))

def select_all_users():
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            users_data = cursor.fetchall()
            return [{'username': user[0], 'password': user[1]} for user in users_data]

if __name__ == '__main__':
    app.run(debug=True)

