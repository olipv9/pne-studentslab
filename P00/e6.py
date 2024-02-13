from seq0 import *
print('Gene U5:')
seq = seq_reverse('../sequences/U5_sequence.fa', 6)
print('Fragment:', seq)
print('Reversed:',seq[::-1])