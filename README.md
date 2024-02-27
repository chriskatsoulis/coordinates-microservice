# coordinates-microservice

A microservice that returns coordinates for a given city. 



## Setting Up

**1) Install ZeroMQ:**
```
pip install zmq

or

pip3 install zmq
```
  
**2) Import ZMQ**
```
import zmq
```
   
**3) Connect socket to talk to server. Use the following verbatim:**
```
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:1107")
```



## How To Request Data

- The microservice expects to receive a string
- Send request by using zmq's send_string() method:
```
location = input("Enter City, State")
socket.send_string(location)
```



## How To Receive Data

- Coordinates are sent as a serialized list in JSON
- Receive coordinates by using zmq's recv_json() method:
```
coordinates_json = socket.recv_json()
```
- Extract coordinates from the coordinates_json variable:
```
latitude = coordinates_json[0]
longitude = coordinates_json[1]
```



## UML Sequence Diagram
![image](https://github.com/chriskatsoulis/coordinates-microservice/assets/122473501/ccdc594e-4b77-4f24-8a8f-2b479f04d8a5)

