import socket
from Client0 import Client


IP = '127.0.0.1'
PORT = 8081
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    # Ask the user for the message
    client_number = input("Enter the number (to exit the program insert 'exit'): ")

    if client_number.lower() == 'exit':
        break
    try:
        client_number_msg = int(client_number)
        client_socket = Client(IP, PORT)
        client_socket.talk(str(client_number_msg))
    except ValueError:
        print(f'You must choose a number between 1-100.')
    except Exception as e:
        print(f'Something went wrong- the error given: {e}')


