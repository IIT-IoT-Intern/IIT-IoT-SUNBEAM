import paho.mqtt.client as mqtt
import mysql.connector

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_home"
)
cursor = db.cursor()

# MQTT connect callback
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT Broker")
    client.subscribe("home/#")

# MQTT message callback
def on_message(client, userdata, message):
    appliance = message.topic.split("/")[1]
    status = message.payload.decode()

    print(f"{appliance} is {status}")

    query = "INSERT INTO appliance_status (appliance_name, status) VALUES (%s, %s)"
    cursor.execute(query, (appliance, status))
    db.commit()

# Create MQTT client
subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Attach callbacks (AFTER functions are defined)
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Connect & listen
subscriber.connect("localhost", 1883)
subscriber.loop_forever()