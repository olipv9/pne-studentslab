from seq0 import *
final_list = ['../sequences/U5_sequence.fa', '../sequences/ADA_sequence.fa','../sequences/FRAT1_sequence.fa','../sequences/FXN_sequence.fa','../sequences/RNU6_269P_sequence.fa']
final_name_list = ['Gene U5','Gene ADA','Gene FRAT1','Gene FXN','Gene RNU6_269P']
for i in final_list:
    num = final_list.index(i)
    length = seq_len(i)
    print(final_name_list[num], '--> Length:', length)
