from sys import argv, exit

if len(argv) != 2:
    if len(argv) < 2:
        exit
    else:
        exit

name_file = argv[1]

d = name_file.find('.')
if name_file[d:] != '.py':
    exit('Not a Python file')

lines = 0

try:
    with open(name_file,'r') as file:
        for line in file:
            if line.isspace():
                continue
            if line.strip().startswith('#'):
                continue
            lines +=1
except FileNotFoundError:
    exit('File does not exist')

print(lines)