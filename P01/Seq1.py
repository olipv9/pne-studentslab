
class Seq:
    def __init__(self, strbases):
        d = ['A', 'T', 'C', 'G']
        for i in strbases:
            if i in d:
                self.strbases = strbases
            else:
                self.strbases = 'ERROR'
        if self.strbases == 'ERROR':
            print('ERROR!!')
        else:
            print('A new sequence was created!')

    def __str__(self):

        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
    for i in seq_list:
        print('Sequence:', seq_list.index(i), '(Length:' + str(i.len()) + ')', i)


def generate_seqs(pattern, number):
    list_1 = []
    count = 1
    error = False
    while not error:
        if count <= number:
            list_1.append(pattern * count)
            count += 1
        else:
            error = True
    return list_1
