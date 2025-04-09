
import paho.mqtt.client as mqtt
import json
from obstacle_handling import generate_response
import logging

logging.basicConfig(filename='subscriber_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def on_message(client, userdata, msg):
    obstacle = json.loads(msg.payload)
    print(f"Obstacle received: {obstacle}")
    logging.info(f"Obstacle received: {obstacle}")
    
    # Εδώ θα πρέπει να γίνεται το publish στο νέο topic drone/commands για την εντολή που θα πρέπει να ακολουθήσει το drone βάσει του εμποδίου
    response = generate_response(obstacle)
    print(f"Response: {response}")
    logging.info(f"Response: {response}\n")

    command = {"source": obstacle, "action": response}
    client.publish("drone/commands", json.dumps(command))

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("drone/obstacles")
client.on_message = on_message
client.loop_forever()
