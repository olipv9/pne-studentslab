
from seq0 import *
filename = ['../sequences/U5_sequence.fa', '../sequences/ADA_sequence.fa','../sequences/FRAT1_sequence.fa','../sequences/FXN_sequence.fa','../sequences/RNU6_269P_sequence.fa']
final_name_list = ['Gene U5:','Gene ADA:','Gene FRAT1:','Gene FXN:','Gene RNU6_269P:']
for i in filename:
    seq_bases = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
    for base in seq_bases.keys():
        seq_bases[base] = seq_count_base(i, base)

for e in final_name_list:
    print(e)
    for key,value in seq_bases.items():
        print(' ', key, ':', value)