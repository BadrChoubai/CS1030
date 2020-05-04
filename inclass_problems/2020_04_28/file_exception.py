default_file = 'a.txt'

try:
    with open(default_file) as input_file:
        for line in input_file.readlines():
            print(line)
except FileNotFoundError:
    print('File not found: {file}'.format(file=default_file))
