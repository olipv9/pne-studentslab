# Create a program for counting the number of bases  in a DNA sequence. The user introduces a sequence of letter representing a DNA chain.
# For example: CATGTAGACTAG.Our program should calculate the total length of the sequence, and the number of bases that in it.
# For the previous example,  the output of our program should look like this:

final_d = {}
user_seq = input('Enter a dna code: ').upper()
length = len(user_seq)
print(length)
for i in user_seq:
    if i not in final_d:
        final_d[i] = 1
    else:
        final_d[i] += 1

for key, value in final_d.items():
    print('The number of', key, 'is :', value)
