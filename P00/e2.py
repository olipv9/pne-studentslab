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

# Example:
filename = '../sequences/ADA_sequence.fa'
sequence = seq_read_fasta(filename)
print("DNA sequence:")
print(sequence)



