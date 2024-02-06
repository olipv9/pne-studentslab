from pathlib import Path
filename = 'sequences/Homo_sapiens_ADA_sequence.fa'
file_contents = Path(filename).read_text()
list_contents = file_contents.split('\n')
list_contents.pop(0) #Elimina el header
print(len(''.join(list_contents)))


#other option
index = file_contents.find('\n')
file_content2 = (file_contents[index:]).replace('\n','')
print(len(file_content2))
