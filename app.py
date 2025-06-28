from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import psycopg2
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Connect to PostgreSQL using environment variables
conn = psycopg2.connect(
    host=os.environ.get('DB_HOST'),
    dbname=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD')
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        return jsonify({'message': 'User already exists'}), 400

    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed))
    conn.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result and bcrypt.check_password_hash(result[0], password):
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'}), 401
name=...
if name == 'main':
    app.run(host="0.0.0.0", port=5000)
