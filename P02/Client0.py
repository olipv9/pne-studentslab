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

    def talk(self, msg=None):
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cs.connect((self.ip, self.port))
        cs.send(str(msg).encode())
        response = cs.recv(2048).decode("utf-8")
        print(f"{response}")
        cs.close()  # Close the socket


