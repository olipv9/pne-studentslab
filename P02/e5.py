from Seq1 import Seq
from Client0 import Client
IP = "212.128.255.75"
PORT = 8080
count = 0
num = 0
s = Seq()
c = Client(IP, PORT)
message = s.read_fasta('../sequences/FRAT1_sequence.fa')
c.talk(f' Sending FRAT1 Gene to the server, in fragments of 10 bases...')
print(f'Gene FRAT1: {message}')
for i in message:
    msg = message[count:count + 10]
    c.talk(f'Fragment {num}: {msg}')
    num += 1
    count = count + 10
    print(f'Fragment {num}: {msg}')
    if count == 50 and num == 5:
        break
