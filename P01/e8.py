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

    def rev_seq(self):
        if self.strbases == 'ERROR!' or self.strbases == 'NULL':
            reversed_seq = self.strbases
        else:
            reversed_seq = self.strbases[::-1]
        return 'NULL' if reversed_seq == '' else reversed_seq

    def complement(self):
        complementary_bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        final_list = []
        for i in self.strbases:
            if i in complementary_bases.keys():
                final_list.append(complementary_bases[i])
        if final_list:
            print('\tComplementary: ',end='')
            for i in final_list:
                print(i, end='')
            print(end='\n')
        else:
            if self.strbases == 'ERROR!':
                print('\tComplementary: ', self.strbases)
            else:
                print('\tComplementary: NULL')


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

