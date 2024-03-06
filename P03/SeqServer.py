import socket
import termcolor
PORT = 8080
IP = "127.0.0.1"
sequences = ['AGAGATAGATATAGSGSCCAGATAGACAGA','CGCGCGCTAGATAGAGCAGAATAGACAGATATAGA','ACACACACACGATATGACAGAGATAGACAAGATAG','AGACAGATAGACAGTTGGACGTCGCTCG']


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Optional: for avoiding the problem of Port already in use
ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        # -- Close the listening socket
        ls.close()
        exit()

    # -- Execute this part if there are no errors
    else:
        num = 0
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        if msg == 'PING' or msg.startswith('PING'):
            print(f"PING command!\nOK!\n")
            response = f"OK!\n"
            cs.send(response.encode())
        elif msg.startswith('GET'):
            msg = msg.split(' ')
            if msg[1] == '1':
                termcolor.cprint(f'GET\n{sequences[0]}','yellow')
                response = f"{sequences[0]}"
                cs.send(response.encode())
            elif msg[1] == '2':
                termcolor.cprint(f'GET\n{sequences[1]}','yellow')
                response = f"{sequences[1]}"
                cs.send(response.encode())
            elif msg[1] == '3':
                termcolor.cprint(f'GET\n{sequences[2]}','yellow')
                response = f"{sequences[2]}"
                cs.send(response.encode())
            elif msg[1] == '4':
                termcolor.cprint(f'GET\n{sequences[3]}','yellow')
                response = f"{sequences[3]}"
                cs.send(response.encode())
            else:
                print('No valid number given')
                response = f'No valid number given'
                cs.send(response.encode())

        cs.close()

