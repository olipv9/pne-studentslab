from seq0 import *
final_list = ['../sequences/U5_sequence.fa', '../sequences/ADA_sequence.fa','../sequences/FRAT1_sequence.fa','../sequences/FXN_sequence.fa','../sequences/RNU6_269P_sequence.fa']
final_name_list = ['Gene U5:','Gene ADA:','Gene FRAT1:','Gene FXN:','Gene RNU6_269P:']
for i in final_list:
    for n in final_name_list:
        if n in i:
            length = seq_len(i)
            print('Gene', n, '--> Length:', length)
