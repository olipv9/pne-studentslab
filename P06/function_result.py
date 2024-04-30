
def get_average(dic_of_bases, s, base):
    num = dic_of_bases[base]
    average = (num * 100) / len(s)
    average = round(average, 2)
    return average, num

def check_for_seq_errors(seq):
    seq = seq.upper()
    seq_bases = ['A', 'C', 'G', 'T']
    valid = True
    for i in seq:
        if i not in seq_bases:
            print(f'The sequence given {seq} is not valid due to invalid characters.')
            valid = False
            break
    return valid

def seq_count(seq):
    dic_bases = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
    for i in seq:
        if i == 'A':
            dic_bases['A'] += 1
        elif i == 'T':
            dic_bases['T'] += 1
        elif i == 'C':
            dic_bases['C'] += 1
        elif i == 'G':
            dic_bases['G'] += 1
    return dic_bases

def get_result(seq):
    try:
        valid_seq = check_for_seq_errors(seq)
        if valid_seq:
            count_bases = seq_count(seq.upper())
            percen_a, num_a = get_average(count_bases, seq, 'A')
            percen_c, num_c = get_average(count_bases, seq, 'C')
            percen_t, num_t = get_average(count_bases, seq, 'T')
            percen_g, num_g = get_average(count_bases, seq, 'G')
            return (f'- A: {num_a} ({percen_a}%)<br>- C: {num_c} ({percen_c}%)'
                    f'<br>- T: {num_t} ({percen_t}%)<br>- G: {num_g} ({percen_g}%) ')
    except Exception as e:
        print(f"An error occurred: {e}")

