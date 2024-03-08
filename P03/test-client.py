from Client0 import Client
import socket

IP = "127.0.0.1"
PORT = 8080
message = Client(IP, PORT)


try:
    message.talk("PING")
    message.talk("GET 0")
    message.talk("INFO AGAGATAGATATAGSGSCCAGATAGACAGA")
    # message.talk("COMP AGAGATAGATATAGSGSCCAGATAGACAGA")
    # message.talk("REV AGAGATAGATATAGSGSCCAGATAGACAGA")
    # message.talk("GENE U5")
except Exception:
    print(f'something just went wrong')

