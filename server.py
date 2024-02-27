# Coordinates Microservice
# Expects "City, State" from client, and replies with latitude, longitude.

import time
import zmq
from geopy.geocoders import Nominatim

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:1107")  # Binds REP socket to tcp://*:1107

while True:
    # Wait for next request from client.
    print("1) Waiting for coordinates request...")
    print()
    city = socket.recv_string()
    print(f"2) Received coordinates request: {city}")

    # Process city, state into coordinates.
    geolocator = Nominatim(user_agent="Coordinates")
    location = geolocator.geocode(city)
    if location:
        coordinates = [location.latitude, location.longitude]
    else:
        coordinates = [None, None]

    # Do some 'work'.
    time.sleep(1)

    # Send coordinates to client.
    print()
    print(f"3) Sending coordinates...")
    print()
    socket.send_json(coordinates)
