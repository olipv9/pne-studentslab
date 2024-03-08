import socket
import termcolor
from Seq1P03 import Seq
from Seq1P03 import percentages

PORT = 8080
IP = "127.0.0.1"
sequences = ['AGAACAGATAGACCCCAGATAGACAGTTG','AGAGATAGATATAGSGSCCAGATAGACAGA','CGCGCGCTAGATAGAGCAGAATAGACAGATATAGA','ACACACACACGATATGACAGAGATAGACAAGATAG','AGACAGATAGACAGTTGGACGTCGCTCG']

# Create functions:
def get_function(number):
    termcolor.cprint(f'GET\n{sequences[number]}\n', 'yellow')
    response = f"{sequences[number]}\n"
    cs.send(response.encode())

# Create the socket
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
    except socket.error:
        print('There has been a problem with the socket.')
        ls.close()
        exit()
    # -- Execute this part if there are no errors
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        if msg == 'PING' or msg.startswith('PING'): #  Ping function
            print(f"PING command!\nOK!\n")
            response = f"OK!\n"
            cs.send(response.encode())

        elif msg.startswith('GET'):  # Get function
            msg = msg.split(' ')
            if msg[1] == '0':
                number_chosen = 0
            elif msg[1] == '1':
                number_chosen = 1
            elif msg[1] == '2':
                number_chosen = 2
            elif msg[1] == '3':
                number_chosen = 3
            elif msg[1] == '4':
                number_chosen = 4
            if 0 <= number_chosen <= 4:
                get_function(number_chosen)
            else:
                print('No valid number given')
                response = f'No valid number given\n'
                cs.send(response.encode())

        elif msg.startswith('INFO'): #  Info function
            (info, seq) = msg.split(' ')
            termcolor.cprint('INFO\n', 'yellow')
            s = Seq(seq)
            print(f'Sequence: {seq}')
            print(f'Total Length: {s.len()}')
            cs.send(f'Sequence: {seq}\nTotal Length: {s.len()}'.encode())
            percentages(seq)
            cs.send(percentages(seq).encode())

        elif msg.startswith('COMP'): # Comp function
            seq = msg.split(' ')[1]
            termcolor.cprint('COMP\n', 'yellow')
            comp_s = Seq(seq)
            final_comp_seq = comp_s.complement()
            print(final_comp_seq)
            cs.send(final_comp_seq.encode())

        elif msg.startswith('REV'): #  Reverse function
            seq = msg.split(' ')[1]
            termcolor.cprint('REV\n', 'yellow')
            rev_s = Seq(seq)
            print(f'{rev_s.rev_seq()}\n')
            cs.send(rev_s.rev_seq().encode())

        elif msg.startswith('GENE'): #  Gene function
            file_dict = {'U5':'../sequences/U5_sequence.fa','ADA': '../sequences/ADA_sequence.fa','FRAT1' :'../sequences/FRAT1_sequence.fa','FXN': '../sequences/FXN_sequence.fa', 'RNU6_269P' :'../sequences/RNU6_269P_sequence.fa'}
            gene_name = msg.split(' ')[1]
            termcolor.cprint('GENE\n', 'yellow')
            gene_s = Seq()
            for i in file_dict:
                if i == gene_name:
                    filename = file_dict[i]
                    break
            gene_s.read_fasta(filename)
            print(f'{gene_s.read_fasta(filename)}\n')
            cs.send(gene_s.read_fasta(filename).encode())








