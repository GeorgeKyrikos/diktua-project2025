# diktua-project2025

# diktua-project2025

Drone Obstacle Detection and Command System

This project implements a drone obstacle detection and command system using MQTT for communication between components. 
The system consists of four Python scripts that work together to detect obstacles, generate appropriate drone commands, and log all activities.
==================================================
Overview
1. drone_subscriber.py
Subscribes to drone commands and logs them
Connects to the MQTT broker on localhost
Subscribes to the drone/commands topic
Logs received commands to both console and drone_log.txt file
Runs indefinitely to process incoming commands

2. obstacle_handling.py
Provides obstacle generation and response logic
generate_obstacle(): Creates random obstacle data including:
Object type (fire, smoke, people, car, tree)
Timestamp
Position coordinates (x, y)
Height
Movement status
generate_response(): Determines appropriate drone response based on obstacle type

3. obstacle_publisher.py
Simulates obstacle detection by publishing random obstacles
Connects to the MQTT broker on localhost
Generates random obstacles every 4 seconds
Publishes obstacles to the drone/obstacles topic
Logs published obstacles to both console and publisher_log.txt file

4. obstacle_subscriber.py
Processes detected obstacles and generates commands
Subscribes to the drone/obstacles topic

For each received obstacle:

Logs the obstacle details
Generates an appropriate response using generate_response()
Publishes a command to the drone/commands topic
Logs all actions to both console and subscriber_log.txt file

System Functions:

obstacle_publisher.py generates and publishes random obstacles

obstacle_subscriber.py receives these obstacles and:

Determines the appropriate drone response
Publishes commands based on the obstacle type

drone_subscriber.py receives and logs these commands

Logs

The system maintains three log files:

publisher_log.txt: Logs all published obstacles
subscriber_log.txt: Logs received obstacles and generated responses
drone_log.txt: Logs all received commands

TODO: 
Heartbeat mechanism for broker failure detection
Drone grouping (random or geographical)
Broker bridges for failover
TLS encryption for security
GPS integration(?)

Note: The scripts should be run seperately in different terminals.
