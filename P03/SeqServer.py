import socket
import termcolor
from Seq1P03 import Seq

PORT = 8080
IP = "127.0.0.1"
sequences = ['AGAACAGATAGACCCCAGATAGACAGTTG', 'AGAGATAGATATAGSGSCCAGATAGACAG', 'CGCGCGCTAGATAGAGCAGAATAGACAGA',
             'ACACACACACGATATGACAGAGATAGACA', 'AGACAGATAGACAGTTGGACGTCGCTCGA']


# Create functions:
def get_function(number):
    termcolor.cprint(f'GET\nGET {number}: {sequences[number]}\n', 'yellow')
    response = f"GET {number}: {sequences[number]}\n"
    cs.send(f'Testing Get...\n{response}'.encode())

def get_average(dic_of_bases, base):
    num = dic_of_bases[base]
    average = (num * 100) / s.len()
    average = round(average, 2)
    return average, num

def check_for_seq_errors(seq):
    seq = seq.upper()
    seq_bases = ['A', 'C', 'G', 'T']
    valid = True
    for i in seq:
        if i not in seq_bases:
            print(f'The sequence given {seq} is not valid due to invalid characters.')
            valid = False
            break
    return valid


# Create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Optional: for avoiding the problem of Port already in use
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
        msg = msg_raw.decode()
        if msg == 'PING' or msg.startswith('PING'):  # Ping function
            print(f"PING command!\nOK!\n")
            response = f"OK!\n"
            cs.send(f'Testing Ping...\n{response}'.encode())

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

        elif msg.startswith('INFO'):  # Info function
            try:
                (info, seq) = msg.split(' ')
                valid_seq = check_for_seq_errors(seq)
                if valid_seq:
                    termcolor.cprint('INFO\n', 'yellow')
                    s = Seq(seq)
                    print(f'Sequence: {seq}')
                    print(f'Total Length: {s.len()}')
                    info_send = f'Testing info...\nSequence: {seq}\nTotal Length: {s.len()}\n'
                    dict_bases_num = s.seq_count()
                    a_average, num_a = get_average(dict_bases_num, 'A')
                    g_average, num_g = get_average(dict_bases_num, 'G')
                    t_average, num_t = get_average(dict_bases_num, 'T')
                    c_average, num_c = get_average(dict_bases_num, 'C')
                    print(f'A: {num_a} ({a_average}%)\nG: {num_g} ({g_average}%)\nT: {num_t} ({t_average}%)\nC: {num_c} '
                          f'({c_average}%)\n ')
                    cs.send((f'{info_send}A: {num_a} ({a_average}%)\nG: {num_g} ({g_average}%)\nT: {num_t} ({t_average}%)\n'
                             f'C: {num_c} ({c_average}%)\n ').encode())
            except Exception as e:
                print(f"An error occurred: {e}")
                cs.close()

        elif msg.startswith('COMP'):  # Comp function
            seq = msg.split(' ')[1]
            valid_seq = check_for_seq_errors(seq)
            if valid_seq:
                termcolor.cprint('COMP\n', 'yellow')
                comp_s = Seq(seq)
                final_comp_seq = comp_s.complement()
                print(f'- Seq: {comp_s}\n- Complementary seq: {final_comp_seq}\n')
                cs.send(f'Testing Comp...\n- Seq: {comp_s}\n- Complementary seq: {final_comp_seq}'.encode())

        elif msg.startswith('REV'):  # Reverse function
            seq = msg.split(' ')[1]
            valid_seq = check_for_seq_errors(seq)
            if valid_seq:
                termcolor.cprint('REV\n', 'yellow')
                rev_s = Seq(seq)
                print(f'- Seq: {rev_s}\n- Reversed seq: {rev_s.rev_seq()}\n')
                cs.send(f'Testing Rev...\n- Seq: {rev_s}\n- Reversed seq: {rev_s.rev_seq()}\n'.encode())

        elif msg.startswith('GENE'):  # Gene function
            file_dict = {'U5': '../sequences/U5_sequence.fa', 'ADA': '../sequences/ADA_sequence.fa',
                         'FRAT1': '../sequences/FRAT1_sequence.fa', 'FXN': '../sequences/FXN_sequence.fa',
                         'RNU6_269P': '../sequences/RNU6_269P_sequence.fa'}
            gene_name = msg.split(' ')[1]
            termcolor.cprint('GENE\n', 'yellow')
            gene_s = Seq()
            for i in file_dict:
                if i == gene_name:
                    filename = file_dict[i]
                    break
            gene_s.read_fasta(filename)
            print(f'Gene {gene_name}: {gene_s.read_fasta(filename)}\n')
            cs.send(f'Testing Gene...\nGene {gene_name}: {gene_s.read_fasta(filename)}'.encode())

        else:
            print(f'The option chosen ({msg}) was not between the ofered ones.')
            cs.send(f'The option chosen ({msg}) was not between the ofered ones.'.encode())
        cs.close()
