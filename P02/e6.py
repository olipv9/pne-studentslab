from Seq1 import Seq
from Client0 import Client
IP = "212.128.255.75"
PORT1 = 8081
PORT2 = 8080
count = 0
num = 1
s = Seq()
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
message = s.read_fasta('../sequences/FRAT1_sequence.fa')
c1.talk(f' Sending FRAT1 Gene to the server, in fragments of 10 bases...')
c2.talk(f' Sending FRAT1 Gene to the server, in fragments of 10 bases...')
print(f'Gene FRAT1: {message}')
for i in message:
    if num > 10:
        break
    else:
        msg = message[count:count + 10]
        if num % 2 == 0:
            c2.talk(f'Fragment {num}: {msg}')
            count = count + 10
        else:
            c1.talk(f'Fragment {num}: {msg}')
            count = count + 10
        print(f'Fragment {num}: {msg}')
        num += 1


