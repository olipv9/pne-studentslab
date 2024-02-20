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

    def most_freq_base(self):
        dic_bases = {}
        highest = 0
        name = ''
        for i in self.strbases.upper():
            if i == 'A' or i == 'G' or i == 'T' or i == 'C':
                if i in dic_bases:
                    dic_bases[i] += 1
                else:
                    dic_bases[i] = 1

        for key, val in dic_bases.items():
            if val > highest:
                highest = val
                name = key
        return name


filenames = ['../sequences/U5_sequence.fa', '../sequences/ADA_sequence.fa','../sequences/FRAT1_sequence.fa','../sequences/FXN_sequence.fa','../sequences/RNU6_269P_sequence.fa']
final_name_list = ['Gene U5:', 'Gene ADA:', 'Gene FRAT1:', 'Gene FXN:', 'Gene RNU6_269P:']

for i in filenames:
    s = Seq()
    s.is_null_sequence()
    s.read_fasta(i)
    num = filenames.index(i)
    print(final_name_list[num], 'Most frequent Base:', s.most_freq_base())

