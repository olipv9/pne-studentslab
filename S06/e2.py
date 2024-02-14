# 2:

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        d = ['A', 'T', 'C', 'G']
        for i in strbases:
            if i in d:
                self.strbases = strbases
            else:
                self.strbases = 'ERROR'

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
    for i in seq_list:
        print('Sequence:', seq_list.index(i), '(Length:' + str(i.len()) + ')', i)


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)

