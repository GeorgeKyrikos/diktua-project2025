from datetime import datetime
import random

objects = ["fire", "smoke", "people", "car", "tree"]
movements = ["spreading", "moving", "stationary"]

def generate_obstacle():
    return {
        "type": "obstacle",
        "timestamp": datetime.now().isoformat(),
        "object": random.choice(objects),
        "position": {"x": random.randint(0, 100), "y": random.randint(0, 100)},
        "height": random.randint(1, 20),
        "movement": random.choice(movements)
    }


def generate_response(obstacle):
    obj = obstacle.get("object", "")
    
    if obj == "fire":
        return "Avoid area, fire detected."
    elif obj == "people":
        return "Go up and slow down."
    elif obj == "tree":
        return "Change direction to avoid the tree."
    elif obj == "bird":
        return "Go up to avoid bird."
    elif obj == "building":
        return "Change route to avoid building."
    else:
        return "Continue monitoring."
