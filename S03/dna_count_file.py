with open('dna.txt', 'r') as f:
    final_d = {}
    count = 0
    for i in f:
        for e in i:
            if e not in final_d:
                final_d[e] = 1
                count += 1
            else:
                final_d[e] += 1
                count += 1
    print('Total length', count)
    print('The number of A:', final_d['A'])
    print('The number of T:', final_d['T'])
    print('The number of C:', final_d['C'])
    print('The number of G:', final_d['G'])


