from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL connection details (same as docker-compose.yml)
db_config = {
    "host": "db",   # service name from docker-compose
    "user": "root",
    "password": "todo",
    "database": "root"
}

@app.route("/")
def home():
    return "Welcome to Flask + MySQL + Nginx App 🚀 sohail. "

@app.route("/users")
def users():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
        cursor.execute("INSERT INTO users (name) VALUES ('Mohammed Sohail Welcome Man')")
        conn.commit()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
