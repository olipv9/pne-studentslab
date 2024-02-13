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
