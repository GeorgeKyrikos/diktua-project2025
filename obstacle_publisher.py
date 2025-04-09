import paho.mqtt.client as mqtt
import json
import time
import logging
from obstacle_handling import generate_obstacle

logging.basicConfig(filename='publisher_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    obs = generate_obstacle()
    client.publish("drone/obstacles", json.dumps(obs))
    print(f"Published obstacle: {obs}")
    logging.info(f"Published obstacle: {obs}\n")
    time.sleep(4)
