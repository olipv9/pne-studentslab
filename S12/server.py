import socket

class Server:
    def __init__(self, ip, port):
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        ls.bind((ip, port))
        ls.listen()
        print("The server is configured!")
        while True:
            # Waits for a client to connect
            print("Waiting for Clients to connect")
            try:
                (cs, client_ip_port) = ls.accept()
            # Server stopped manually
            except KeyboardInterrupt:
                print("Server stopped by the user")
                # -- Close the listening socket
                ls.close()
                exit()
            except socket.error:
                print('There has been a problem with the socket.')
                ls.close()
                exit()
            # Execute this part only if there are no errors
            else:
                print("A client has connected to the server!")
                msg_raw = cs.recv(2048)
                msg = msg_raw.decode()
                self.msg = msg
                self.cs = cs

    def give_it_back(self):
        return self.msg, self.cs
