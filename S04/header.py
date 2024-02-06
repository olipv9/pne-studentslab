from pathlib import Path
# -- Constant with the new of the file to open
filename = 'sequences/Homo_sapiens_RNU6_269P_sequence.fa'
file_contents = Path(filename).read_text()
list_content = file_contents.split('\n')
print(list_content[0])

