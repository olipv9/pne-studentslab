# 1:
class Seq:
    def __init__(self, strbases):
        d = ['A', 'T', 'C', 'G']
        for i in strbases:
            if i in d:
                self.strbases = strbases
            else:
                self.strbases = 'ERROR'
                break
        if self.strbases == 'ERROR':
            print('ERROR!!')
        else:
            print('A new sequence was created')

    def __str__(self):

        return self.strbases

    def len(self):
        return len(self.strbases)


s1 = Seq("AGTACACTGGT")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")


