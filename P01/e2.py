#The first you should do in the __init()__ method is checking if it is a null sequence.
# If so, print the message on the console, assign the value to the self.strbases attribute and return.
# If it is not null, continue with the other checks.
class Seq:
    def __init__(self, strbases=""):
        d = ['A', 'T', 'C', 'G']
        for i in strbases:
            if i not in d:
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
        return len(self.strbases)

    def is_null_sequence(self):
        if self.strbases == '':
            print('Null sequence created.')
        return 'NULL' if self.strbases == '' else self.strbases

# -- Creating a Null sequence
s1 = Seq()
s2 = Seq("TATAC")

print('Sequence 1:', s1.is_null_sequence())
print('Sequence 2:', s2.is_null_sequence())


