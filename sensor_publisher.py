#What I learned:
#   - how to publish random sensor data using MQTT (a message protocol)
#   - publish/subscribe messaging in IoT devices
#   - how to control embedded systems
#What I accomplished: 
#   - simulated a real-world sensor by acting like one
#   - generated test data to simulate sensors
#   - built the MQTT

import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "bioreactor/temperature"

client = mqtt.Client()
#Connect to the MQTT broker (localhost)
#1883 is the default MQTT port number without encryption (unsecured)
#60 is the keepalive internal, which means the client has 60 seconds to tell the broker it's still alive
client.connect(BROKER, 1883, 60)

while True:
    #Simulate sensor data, rounded to two decimal places
    temperature = round(random.uniform(36.0, 38.0,), 2)
    client.publish(TOPIC, f"(temperature)")
    print(f"Published temperature: {temperature}°C")
    #Publish data to the topic (bioreactor/temperature) every two seconds
    time.sleep(2)