import socket

# SERVER IP, PORT
PORT = 8081
IP = "127.0.0.1"

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

print(f"Server listening on {IP}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    client_message = client_socket.recv(2048).decode()
    print(f"Received message from client: {client_message}")

    response = f"Server received: {client_message}"
    client_socket.send(response.encode())

    client_socket.close()
