# Implement the seq_read_fasta(filename) function.
# It should open a file in FASTA format and return a String with the DNA sequence.
# The header is removed as well as the '\n' characters.


def seq_read_fasta(filename):
    final = filename.split('/')
    print('Folder:', final[1], '\nFilename:', final[2])
    from pathlib import Path
    file_contents = Path(filename).read_text()
    list_content = file_contents.split('\n')
    list_content.pop(0)


seq_read_fasta('../sequences/U5_sequence.fa')



