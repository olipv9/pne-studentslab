import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.75"  # this IP address is local, so only requests from the same machine are possible (también puedes copiar poniendo esto en el terminal- hostname -I)

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
while True:
    (rs, address) = ls.accept()
    print(f'Client {address}')
    rs.close()
    msg = rs.recv(2048).decode('utf-8')
    print('client says...')
    new_msg = "I'm a happy server"
    rs.send(new_msg.encode())

# -- Close the socket
ls.close()


