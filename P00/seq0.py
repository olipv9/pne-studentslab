# Test function. It just prints (for the moment) the "OK" message on the console
def seq_ping():
    print('ok')
# 2:
def seq_read_fasta(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:])
            sequence = seq_joined[:20]
    except FileNotFoundError:
        print("Error: File", filename, "not found.")
        sequence = None
    return sequence

# 3:
def seq_len(seq):
    sequence = ''
    with open(seq, 'r') as f:
        header = next(f)
        for line in f:
            sequence += line.strip('\n')
    return len(sequence)

# 4:
def seq_count_base(seq, base):
    try:
        with open(seq, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:])
    except FileNotFoundError:
        print("Error: File", seq, "not found.")
        count_base = None
    else:
        count_base = 0
        for i in seq_joined:
            if i == base.upper():
                count_base += 1
            else:
                pass
    return count_base

# 5:


def seq_count(seq):
    try:
        with open(seq, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:])
    except FileNotFoundError:
        print("Error: File", seq, "not found.")
        dic_bases = {}
    else:
        dic_bases = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
        for i in seq_joined:
            if i == 'A':
                dic_bases['A'] += 1
            elif i == 'T':
                dic_bases['T'] += 1
            elif i == 'C':
                dic_bases['C'] += 1
            elif i == 'G':
                dic_bases['G'] += 1
    return dic_bases

# 6:


def seq_reverse(seq, n):
    try:
        with open(seq, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:])
            sequence = seq_joined[:n]
    except FileNotFoundError:
        print("Error: File", seq, "not found.")
        sequence = None
    return sequence




# 7:


def seq_complement(seq):
    complementary_bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    try:
        with open(seq, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:]).replace('\n','')
    except FileNotFoundError:
        print("Error: File", seq, "not found.")
        sequence = None
    else:
        print('Fragment:', seq_joined)
        print('Complementary: ', end='')
        for i in seq_joined:
            if i in complementary_bases.keys():
                print(complementary_bases[i], end='')


# 8:

def most_freq_base(seq):
    try:
        with open(seq, 'r') as file:
            lines = file.readlines()
            seq_joined = ''.join(lines[1:]).replace('\n','')
    except FileNotFoundError:
        print("Error: File", seq, "not found.")
        sequence = None
    else:
        dic_bases = {}
        highest = 0
        name = ''
        for i in seq_joined.upper():
            if i == 'A' or i == 'G' or i == 'T' or i == 'C':
                if i in dic_bases:
                    dic_bases[i] += 1
                else:
                    dic_bases[i] = 1

        for key, val in dic_bases.items():
            if val > highest:
                highest = val
                name = key
        return name