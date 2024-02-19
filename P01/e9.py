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
            print('\tComplementary: ', end='')
            for i in final_list:
                print(i, end='')
            print(end='\n')
        elif self.strbases == 'ERROR!':
            print('\tComplementary: ', self.strbases)
        else:
            print('\tComplementary: NULL')

    def read_fasta(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.strbases = ''.join(lines[1:]).replace('\n', '')
        except FileNotFoundError:
            print("Error: File", filename, "not found.")
            self.strbases = None
        return self.strbases

    def seq_count(self):
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
        return dic_bases


s = Seq()
s.read_fasta('../sequences/U5_sequence.fa')
print('Sequence:', '(Length: ' + str(s.len()) + ')', s.is_null_sequence())
print('\tBases:', s.seq_count())
print('\tReversed:', s.rev_seq())
s.complement()
