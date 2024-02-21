from Seq1 import Seq

s = Seq()
s.read_fasta('../sequences/U5_sequence.fa')
print('Sequence:', '(Length: ' + str(s.len()) + ')', s)
print('\tBases:', s.seq_count())
print('\tReversed:', s.rev_seq())
s.complement()
