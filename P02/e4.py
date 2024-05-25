from Seq1 import Seq
from Client0 import Client
import termcolor
IP = "127.0.0.1"
PORT = 8081
s1 = Seq()
s2 = Seq()
s3 = Seq()
c = Client(IP, PORT)


filenames = [s1.read_fasta('../sequences/U5_sequence.fa'), s2.read_fasta('../sequences/ADA_sequence.fa'), s3.read_fasta('../sequences/FRAT1_sequence.fa')]
final_name_list = ['U5', 'ADA', 'FRAT1']

for i in final_name_list:
    index = final_name_list.index(i)
    print('To server:', end=' ')
    termcolor.cprint(f'Sending {i} Gene to the server...', 'blue')
    print('From server:\n')
    termcolor.cprint(c.talk(f'Sending {i} Gene to the server...'), 'green')
    print('To server:', end=' ')
    termcolor.cprint(str(filenames[index]), 'blue')
    print('From server: \n ')
    termcolor.cprint(c.talk(str(filenames[index])), 'green')








