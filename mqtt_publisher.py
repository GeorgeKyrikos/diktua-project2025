import paho.mqtt.client as mqtt
import json
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.loop_start()

object_types = ["Airplane", "Boat", "Building", "Car", "Drone", "Motorcycle", "Tree"]
rubbish_types = ["Waste", "Recyclable Materials"]
disaster_types = ["Fire", "Flood", "Car Accident"]
movements = ["Stationary", "Moving"]

def generate_object():
    return {
        "type": "object",
        "object": random.choice(object_types),
        "position": {"x": random.randint(0, 50), "y": random.randint(0, 50)},
        "height": random.randint(1, 20),
        "movement": random.choice(movements)
    }

def generate_rubbish():
    return {
        "type": "rubbish",
        "object": random.choice(rubbish_types),
        "position": {"x": random.randint(0, 50), "y": random.randint(0, 50)}
    }

def generate_disaster():
    return {
        "type": "disaster",
        "event": random.choice(disaster_types),
        "severity": random.choice(["low", "medium", "high"]),
        "location": {"x": random.randint(0, 50), "y": random.randint(0, 50)}
    }

while True:

    object_data = generate_object()
    client.publish("drone/objects", json.dumps(object_data), qos=0)
    print(f"[objects] Sent: {json.dumps(object_data)}")

    rubbish_data = generate_rubbish()
    client.publish("drone/rubbish", json.dumps(rubbish_data), qos=1)
    print(f"[rubbish] Sent: {json.dumps(rubbish_data)}")

    disaster_data = generate_disaster()
    client.publish("drone/disaster", json.dumps(disaster_data), qos=2)
    print(f"[disaster] Sent: {json.dumps(disaster_data)}")

    time.sleep(3)


# NEXT STEPS

# IMPLEMENT A HEARTBEAT MECHANISM FOR BROKERS (NOTIFY IN CASE OF FAILURE)
# DIVIDE DRONES INTO GROUPS (AT RANDOM OR USING ALGORITHM BASED ON GEOGRAPHICAL POSITION)
# CREATE BROKER BRIDGES (TO ENABLE ACTIVE BROKERS TAKING OVER DEAD GROUPS)
# TLS ENCRYPTION FOR SECURITY
# GPS (?)