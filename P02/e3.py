from Client0 import Client
import socket
IP = "212.128.255.64"
PORT = 8081

c = Client(IP, PORT)
print("Sending a message to the server...")
response = c.talk(" Testing !!!")
print(f"Response: {response}")
