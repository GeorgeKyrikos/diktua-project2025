
import paho.mqtt.client as mqtt
import json
import logging

logging.basicConfig(filename='drone_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print(f"Command received: {data['source']}")
    logging.info(f"Command received: {data['source']}")

    print(f"Command received: {data['action']}")
    logging.info(f"Command received: {data['action']}\n")


client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("drone/commands")
client.on_message = on_message
client.loop_forever()
