from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import time

app = Flask(__name__)

def get_db_connection():
    # Retry logic because MySQL takes time to start
    retries = 5
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="password",
                database="mydb"
            )
            return conn
        except mysql.connector.Error:
            retries -= 1
            time.sleep(2)
    return None

def init_db():
    retries = 10
    while retries > 0
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="password",
                database="mydb"
            )
            cursor = conn.cursor()
            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    message TEXT NOT NULL
                )
            """)
            # Add a default message if empty
            cursor.execute("SELECT COUNT(*) FROM messages")
            if cursor.fetchone()[0] == 0:
                cursor.execute("INSERT INTO messages (message) VALUES ('Hello from Dockerized MySQL!')")
            conn.commit()
            cursor.close()
            conn.close()
            print("Database initialized successfully!")
            return
        except mysql.connector.Error as e:
            retries -= 1
            print(f"Database init failed, retrying... ({retries} retries left): {e}")
            time.sleep(2)
    print("Failed to initialize database after retries")

@app.route('/')
def index():
    conn = get_db_connection()
    if not conn:
        return "<h1>Error: Could not connect to Database. Try refreshing in 10 seconds.</h1>"
    
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM messages")
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    new_msg = request.form.get('message')
    if new_msg:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (message) VALUES (%s)", (new_msg,))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)