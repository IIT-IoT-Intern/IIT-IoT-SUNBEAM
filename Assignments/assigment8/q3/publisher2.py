import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883

client = mqtt.Client(
    client_id="Snehit_Publisher",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.connect(BROKER, PORT, 60)

while True:
    temp = round(random.uniform(25, 35), 2)
    hum = round(random.uniform(50, 75), 2)

    client.publish("Snehit/sensor/temperature", temp)
    client.publish("Snehit/sensor/humidity", hum)

    print(f"Published Temp: {temp}")
    print(f"Published Hum: {hum}")
    print("----------------------")

    time.sleep(3)