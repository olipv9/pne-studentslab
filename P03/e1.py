import socket
PORT = 8080
IP = "127.0.0.1"
class Seq:
    bases_list = ['A', 'T', 'C', 'G']
    def __init__(self):
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Optional: for avoiding the problem of Port already in use
        ls.bind((IP, PORT))
        ls.listen()
        print("The server is configured!")
        while True:
            print("Waiting for Clients to connect")
            try:
                (cs, client_ip_port) = ls.accept()
                self.cs = cs
                self.client_ip_port = client_ip_port
            except KeyboardInterrupt:
                print("Server stopped by the user")
                # -- Close the listening socket
                ls.close()
                exit()

            # -- Execute this part if there are no errors
            else:
                print("A client has connected to the server!")
                msg_raw = cs.recv(2048)
                msg = msg_raw.decode()
                self.msg = msg

    def respond_client(self):
        if msg == 'PING' or msg.startswith('PING'):
            print(f"OK!\n")
            response = f"OK!\n"
            cs.send(response.encode())
        cs.close()

