'''
Program Two - Word Search Engine
'''
import sys


def cleanse_input(lines: list) -> list:
    for i, line in enumerate(lines):
        if '\n' in line:
            lines[i] = line.replace('\n', '')

    return lines


def read_file(file_path: str) -> list:
    try:
        with open(file_path) as file:
            return cleanse_input(file.readlines())
    except FileNotFoundError:
        print('File not found: ', file_path)


input_file = 'dictionary.txt'
while True:
    search_letter = input('Give me a letter to search the dictionary with: ')

    if search_letter.isalpha() and len(search_letter) == 1:
        search_letter = search_letter.upper()
        dictionary = read_file(input_file)

        if search_letter in dictionary:
            search_index = dictionary.index(search_letter)
            print(dictionary[search_index+1])
            sys.exit()
        else:
            print('Double check the value you entered.')
