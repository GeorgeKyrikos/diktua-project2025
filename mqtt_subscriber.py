import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    try:
        payload_str = msg.payload.decode("utf-8")
        data = json.loads(payload_str)

        print(f"Topic: {msg.topic}")
        print(f"Message: {json.dumps(data)}")

        if msg.topic == "drone/disaster":
            print("Disaster detected")
        elif msg.topic == "drone/rubbish":
            print("Garbage detected")
        elif msg.topic == "drone/objects":
            print("Object detected.")
    except Exception as e:
        print(f"Error decoding message on topic {msg.topic}: {e}")
        print(f"Raw payload: {msg.payload}")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("drone/#")  # Subscribe to all folders

print("Subscriber listening...")
client.loop_forever()
