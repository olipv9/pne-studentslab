from Client0 import Client
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((self.ip, self.port))

# Send data.
s.send(str.encode(msg))

# Receive data
response = s.recv(2048).decode("utf-8")

# Close the socket
s.close()

# Return the response
return response
