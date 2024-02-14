import termcolor

# 1:


class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        error = None
        for i in self.strbases:
            if i == 'A' or i == 'G' or i == 'T' or i == 'C':
                error = None
            else:
                error = 1
        if error == 1:
            print('ERROR !!')
            self.strbases = 'ERROR'
        else:
            print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        return len(self.strbases)


s1 = Seq("AGTACACTGGT")
s2 = Seq("Hello? Am I a valid sequence?")
termcolor.cprint(f"Sequence 1: {s1}",'red')
termcolor.cprint(f"Sequence 2: {s2}",'blue')
