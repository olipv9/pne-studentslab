import socket
class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print('OK!')
        return self.ip

    def __str__(self):
        return f'Connection to SERVER at {self.ip}, at PORT {self.port}'

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))  # Send data.
        response = s.recv(2048).decode("utf-8")  # Receive data
        s.close()  # Close the socket
        return response

