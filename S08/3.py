import socket

# SERVER IP, PORT
PORT = 8081
IP = "127.0.0.1"

while True:
    # Ask the user for the message
    user_message = input("Enter your message (to exit the program insert 'exit'): ")

    if user_message.lower() == 'exit':
        break
    # Create the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Establish the connection to the Server
        client_socket.connect((IP, PORT))
        # Send the user message
        client_socket.send(user_message.encode())
        # Receive and print the server's response
        server_response = client_socket.recv(2048).decode()
        print(f"Server response: {server_response}")
    except Exception as e:
        print(f" An error occurred : {e}")
    finally:
        # Close the socket
        client_socket.close()



