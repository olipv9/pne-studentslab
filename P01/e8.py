from Seq1 import Seq

s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("TAXXXC")

print('Sequence 1:', '(Length:' + str(s1.len()) + ')', s1.is_null_sequence())
print('\tReversed:', s1.rev_seq())
s1.complement()

print('Sequence 2:', '(Length:' + str(s2.len()) + ')', s2.is_null_sequence())
print('\tReversed:', s2.rev_seq())
s2.complement()

print('Sequence 3:', '(Length:' + str(s3.len()) + ')', s3.is_null_sequence())
print('\tReversed:', s3.rev_seq())
s3.complement()
