import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

BROKER = "broker.hivemq.com"
PORT = 1883

TEMP_THRESHOLD = 32
HUM_THRESHOLD = 65

# ---------- DATABASE CONNECTION ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)

cursor = db.cursor()

# ---------- CALLBACKS ----------
def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected to MQTT Broker")
    client.subscribe("snehit/sensor/temperature")
    client.subscribe("snehit/sensor/humidity")

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8", errors="ignore").strip()

    if payload == "":
        return

    try:
        value = float(payload)
    except ValueError:
        return

    timestamp = datetime.now()

    if msg.topic == "snehit/sensor/temperature":
        print(f"Temperature: {value} °C")

        cursor.execute(
            "INSERT INTO sensor_data (sensor_type, value, timestamp) VALUES (%s, %s, %s)",
            ("temperature", value, timestamp)
        )
        db.commit()

        if value > TEMP_THRESHOLD:
            print("⚠ ALERT: High Temperature")

    elif msg.topic == "snehit/sensor/humidity":
        print(f"Humidity: {value} %")

        cursor.execute(
            "INSERT INTO sensor_data (sensor_type, value, timestamp) VALUES (%s, %s, %s)",
            ("humidity", value, timestamp)
        )
        db.commit()

        if value > HUM_THRESHOLD:
            print("⚠ ALERT: High Humidity")

# ---------- CLIENT ----------
client = mqtt.Client(
    client_id="snehit_Subscriber",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
