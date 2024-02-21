from Seq1 import Seq

filenames = ['../sequences/U5_sequence.fa', '../sequences/ADA_sequence.fa','../sequences/FRAT1_sequence.fa', '../sequences/FXN_sequence.fa','../sequences/RNU6_269P_sequence.fa']
final_name_list = ['Gene U5:', 'Gene ADA:', 'Gene FRAT1:', 'Gene FXN:', 'Gene RNU6_269P:']

for i in filenames:
    s = Seq()
    s.read_fasta(i)
    num = filenames.index(i)
    print(final_name_list[num], 'Most frequent Base:', s.most_freq_base())
