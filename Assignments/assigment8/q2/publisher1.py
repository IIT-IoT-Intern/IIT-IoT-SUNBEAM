import paho.mqtt.client as mqtt
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

while True:
    client.publish("home/light", "ON")
    print("Light ON")
    time.sleep(2)
    client.publish("home/light", "OFF")
    print("Light OFF")
    time.sleep(2)
    client.publish("home/fan", "ON")
    print("Fan ON") 
    time.sleep(2)                   
    client.publish("home/fan", "OFF")
    print("Fan OFF")
    time.sleep(2)