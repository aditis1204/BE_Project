####Remove first line in file
from automate1 import func1
with open('filename1', 'r') as fin:
    data = fin.read().splitlines(True)
with open('filename1', 'w') as fout:
    fout.writelines(data[1:])

func1()
