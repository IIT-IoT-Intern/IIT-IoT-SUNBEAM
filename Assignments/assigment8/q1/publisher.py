import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"   # or public broker like "broker.hivemq.com"
port = 1883

client = mqtt.Client()
client.connect(broker, port)

while True:
    ldr_value = random.randint(0, 1023)
    temp_value = round(random.uniform(20, 40), 2)

    client.publish("sensor/ldr", ldr_value)
    client.publish("sensor/lm35", temp_value)

    print("Published LDR:", ldr_value)
    print("Published Temperature:", temp_value)

    time.sleep(5)
