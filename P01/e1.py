from Seq1 import Seq


def print_seqs(seq):
    count = 0
    for i in seq:
        count += 1
    print('Sequence', str(count) + ': (Length: ' + str(len(seq)) + ')', seq)


Seq('ACTGA')
print_seqs('ACTGA')
