import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "bioreactor/temperature"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    temperature = round(random.uniform(36.0, 38.0,), 2)
    client.publish(TOPIC, f"(temperature)")
    print(f"Published temperature: {temperature}°C")
    time.sleep(2)