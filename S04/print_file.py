from pathlib import Path
from pathlib import Path
# -- Constant with the new of the file to open
filename = '../sequences/RNU6_269P_sequence.fa'
# -- Open and read the file
file_contents = Path(filename).read_text()
# -- Print the contents on the console
print(file_contents)
