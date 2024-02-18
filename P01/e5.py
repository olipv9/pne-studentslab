class Seq:
    def __init__(self, strbases=""):
        d = ['A', 'T', 'C', 'G']
        self.valid_sequence = True

        for i in strbases:
            if i not in d:
                self.valid_sequence = False
                self.strbases = 'ERROR!'
                print('Invalid sequence!')
                break
        else:
            self.strbases = strbases
            if self.strbases == strbases and strbases != "":
                print('A new sequence was created!')

    def __str__(self):
        return self.strbases

    def len(self):
        return '0' if self.strbases == 'ERROR!' else len(self.strbases)

    def is_null_sequence(self):
        if self.strbases == '' and self.valid_sequence:
            print('Null sequence created.')
        return 'NULL' if self.strbases == '' else self.strbases


    def count_base(self, base):
        count_base = 0
        for i in self.strbases:
            if i == base:
                count_base += 1
        return count_base


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

