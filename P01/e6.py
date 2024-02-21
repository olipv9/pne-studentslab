from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("TAXXXC")

print('Sequence 1:', '(Length:' + str(s1.len()) + ')', s1.is_null_sequence())
print(s1.seq_count())
print('Sequence 2:', '(Length:' + str(s2.len()) + ')', s2.is_null_sequence())
print(s2.seq_count())
print('Sequence 3:', '(Length:' + str(s3.len()) + ')', s3.is_null_sequence())
print(s3.seq_count())




