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


    def count(self):
        dic_bases = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
        for i in self.strbases:
            if i == 'A':
                dic_bases['A'] += 1
            elif i == 'T':
                dic_bases['T'] += 1
            elif i == 'C':
                dic_bases['C'] += 1
            elif i == 'G':
                dic_bases['G'] += 1
            else:
                break
        return dic_bases

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("TAXXXC")

print('Sequence 1:', '(Length:' + str(s1.len()) + ')', s1.is_null_sequence())
print(s1.count())
print('Sequence 2:', '(Length:' + str(s2.len()) + ')', s2.is_null_sequence())
print(s2.count())
print('Sequence 3:', '(Length:' + str(s3.len()) + ')', s3.is_null_sequence())
print(s3.count())


