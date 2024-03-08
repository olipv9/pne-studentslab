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
            else:
                self.strbases = 'NULL'
                print(' Null sequence was created!')
                self.valid_sequence = False


    def __str__(self):
        return self.strbases

    def len(self):
        return '0' if not self.valid_sequence else len(self.strbases)

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
        if not final_list:
            if self.strbases == 'ERROR!':
                final_answer = f'Complementary: {self.strbases}'
            else:
                final_answer = f'Complementary: NULL'
        else:
            final_answer = ''.join(final_list)
        return final_answer

    def read_fasta(self, filename):
        self.valid_sequence = True
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.strbases = ''.join(lines[1:]).replace('\n', '')
        except FileNotFoundError:
            print("Error: File", filename, "not found.")
            self.strbases = None
        return self.strbases

    def count_base(self, base):
        count_base = 0
        for i in self.strbases:
            if i == base:
                count_base += 1
        return count_base

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


def percentages(seq):
    dict_bases_num = seq.seq_count()
    dict_bases_average = {}
    for base, num in dict_bases_num.items():
        average = (num * 100) / s.len()
        average = round(average, 2)
        print(f'{base}: {num} ({average}%)')
