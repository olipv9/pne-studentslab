import termcolor

class Seq:
    def __init__(self, strbases):
        d = ['A', 'T', 'C', 'G']
        for i in strbases:
            if i in d:
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = 'ERROR'

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


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


seq_list = generate_seqs('A', 3)
print(seq_list)


print('List 1:')
seq_list = generate_seqs('A', 3)
for i in seq_list:
    y = f'Sequence:{seq_list.index(i)} (Length:{str(len(i))}) {i}'
    termcolor.cprint(y, 'green')

print('List 2:')
seq_list = generate_seqs('AC', 4)
for i in seq_list:
    x = f'Sequence: {seq_list.index(i)} (Length:{str(len(i))}) {i}'
    termcolor.cprint( x, 'blue')

