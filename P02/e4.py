from Seq1 import Seq
from Client0 import Client
IP = "212.128.255.64"
PORT = 8081
s = Seq()
c = Client(IP, PORT)
message = s.read_fasta('../sequences/U5_sequence.fa')
c.talk(message)
