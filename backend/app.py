from flask import Flask, jsonify
import mysql.connector
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # active CORS pour toutes les routes
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "dbflask")
@app.route("/api/users")
def get_users():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)