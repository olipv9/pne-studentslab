class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print('OK!')
        return self.ip

    def __str__(self):
        return f'Connection to SERVER at {self.ip}, at PORT {self.port}'
