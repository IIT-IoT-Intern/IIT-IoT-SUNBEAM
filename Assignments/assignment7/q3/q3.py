from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "smarthome.db"

# ---------- Database Setup ----------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS smart_home (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            light TEXT,
            fan TEXT,
            temperature REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- Route: Update Sensor Data ----------
@app.route('/update', methods=['POST'])
def update_status():
    data = request.json

    light = data.get('light')          # ON / OFF
    fan = data.get('fan')              # ON / OFF
    temperature = data.get('temperature')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO smart_home (light, fan, temperature, timestamp)
        VALUES (?, ?, ?, ?)
    """, (light, fan, temperature, timestamp))
    conn.commit()
    conn.close()

    return jsonify({"message": "Sensor data updated successfully"}), 201

# ---------- Route: Get Current Status ----------
@app.route('/status', methods=['GET'])
def get_status():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT light, fan, temperature, timestamp
        FROM smart_home
        ORDER BY id DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "Light Status": row[0],
            "Fan Status": row[1],
            "Temperature": row[2],
            "Last Updated": row[3]
        })
    else:
        return jsonify({"message": "No data available"}), 404

# ---------- Run Server ----------
if __name__ == '__main__':
    app.run(debug=True)
