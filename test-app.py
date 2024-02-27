# Simple program to test the Coordinates Microservice.
# Sends "City, State" to server, expects latitude, longitude in return.

import zmq
import time

context = zmq.Context()

# Socket to talk to server.
print("Connecting to Server…")
time.sleep(2)
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:1107")  # Connects REQ socket to tcp://localhost:1107

while True:
    # Clear screen.
    print("\033[H\033[J")

    # Display application name.
    print("""
  _____                 ___           __        
 / ___/__  ___  _______/ (_)__  ___ _/ /____ ___
/ /__/ _ \/ _ \/ __/ _  / / _ \/ _ `/ __/ -_|_-<
\___/\___/\___/_/  \_,_/_/_//_/\_,_/\__/\__/___/
                                                """)

    # Ask user to enter City, State, and send request.
    print()
    location = input("ENTER CITY, STATE: ")
    print(f"Requesting coordinates for {location}...")
    socket.send_string(location)

    # Receive the coordinates.
    coordinates_json = socket.recv_json()
    print()
    print()
    print(f"Received coordinates for {location}:")

    # Decode the JSON and extract coordinates.
    latitude = coordinates_json[0]
    longitude = coordinates_json[1]
    print(f"Latitude: {coordinates_json[0]}, Longitude: {coordinates_json[1]}")
    print()
    print()
    print()
    print()
    print()
    input("Press enter to find another City, State...")
