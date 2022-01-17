input_file = 'dictionary.txt'

try:
    dictionary = open(input_file, 'r')
except FileNotFoundError as error:
    print(error)
else:
    for line in dictionary:
        print(line.replace('\n', ''))

    dictionary.close()
