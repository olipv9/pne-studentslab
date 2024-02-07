from pathlib import Path
filename = '../sequences/U5_sequence.fa'
file_contents = Path(filename).read_text()
list_content = file_contents.split('\n')
for i in range(1,len(list_content)):
    print(list_content[i])
