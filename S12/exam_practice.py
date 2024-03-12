# 1. At the start, the Game generates a random number between 1 and 100.
# 2. The Player submits a guess trying to figure out the generated number.
# 3. The Game responds with hints of "higher" or "lower" in relation to the generated number.
# 4. The process is repeated until the Player finds the number.
# 5. The game displays how many attempts it took to find the number.
import socket
import random


IP = '127.0.0.1'
PORT = 8081


def generate_the_num():
    secret_number = random.randint(1, 100)
    return secret_number

class Guessnum:
    def __init__(self, client_num):
        self.client_num = client_num
        self.secret_number = generate_the_num()

    def guess(self, client_socket):
        attempt_num = []
        if self.client_num == self.secret_number:
            print(f'The correct number was chosen')
            client_socket.send(f'You won after {attempt_num[-1]} attempts'.encode())
        else:
            attempt_num.append(self.client_num)
            if int(self.client_num) < int(self.secret_number) and 1 < int(self.client_num) < 100:
                print(f'Chose a higher number.')
                client_socket.send(f'Chose a higher number (previous = {self.client_num}).'.encode())
            elif int(self.client_num) > int(self.secret_number) and 1 < int(self.client_num) < 100:
                print(f'Chose a lower number.')
                client_socket.send(f'Chose a lower number (previous = {self.client_num}).'.encode())
            else:
                print('The number chosen was not within the range (1-100).')
                client_socket.send(f'The number chosen was not within the range (1-100).'.encode())


# Generate my server
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
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
        number_client = msg_raw.decode()
        guess_the_num = Guessnum(number_client)
        correct = guess_the_num.guess(cs)
        cs.close()



