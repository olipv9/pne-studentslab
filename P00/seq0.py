# Test function. It just prints (for the moment) the "OK" message on the console
def seq_ping():
    print('ok')
# 2:
def seq_read_fasta(filename):
    final = filename.split('/')
    print('Folder:', final[1], '\nFilename:', final[2])
    from pathlib import Path
    file_contents = Path(filename).read_text()
    list_content = file_contents.split('\n')
    list_content.pop(0)
# 3:


def seq_len(seq):
    sequence = ''
    with open(seq, 'r') as f:
        header = next(f)
        for line in f:
            sequence += line.strip('\n')
    return len(sequence)
