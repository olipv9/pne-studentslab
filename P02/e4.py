from Seq1 import Seq
from Client0 import Client
import termcolor
IP = "212.128.255.75"
PORT = 8081
s = Seq()
c = Client(IP, PORT)
message = s.read_fasta('../sequences/U5_sequence.fa')
print('To server:', end=' ')
termcolor.cprint('Sending U5 Gene to the server...','blue')
print('From server:\n')
termcolor.cprint(c.talk('Sending U5 Gene to the server...'), 'green')
print('To server:', end=' ')
termcolor.cprint(message, 'blue')
print('From server: \n ')
termcolor.cprint(c.talk(message), 'green')








