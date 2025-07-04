from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import psycopg2
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

import time

DATABASE_URL = os.environ.get('DATABASE_URL')

# Retry loop to wait for PostgreSQL to be ready
for i in range(10):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        break
    except psycopg2.OperationalError:
        print("Postgres not ready yet, retrying in 2 seconds...")
        time.sleep(2)
else:
    raise Exception("Could not connect to Postgres after 10 attempts")

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
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

