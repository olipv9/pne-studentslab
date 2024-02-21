from Seq1 import Seq


def count_all_bases(seq):
    base_l = ['A', 'T', 'G', 'C']
    num_list = []
    for letter in base_l:
        num = seq.count_base(letter)
        num_list.append(num)
    print(f'A: {num_list[0]}, T: {num_list[1]}, G: {num_list[2]}, C: {num_list[3]}')


s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("TAXXXC")

print('Sequence 1:', '(Length:' + str(s1.len()) + ')', s1.is_null_sequence())
count_all_bases(s1)
print('Sequence 2:', '(Length:' + str(s2.len()) + ')', s2.is_null_sequence())
count_all_bases(s2)
print('Sequence 3:', '(Length:' + str(s3.len()) + ')', s3.is_null_sequence())
count_all_bases(s3)

