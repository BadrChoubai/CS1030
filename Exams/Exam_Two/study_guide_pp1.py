'''
Practice Program One - User Created Dictionary
'''
import sys


def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            for letter in sorted(content.keys()):
                file.write(f'{letter}\n' +
                           ', '.join(sorted(content[letter])) + '\n')
    except FileNotFoundError:
        print('File not found', file_path)


output_file = 'dictionary.txt'
dictionary = {}
while True:
    word_input = input("Give me a word: ")

    if word_input == '':
        write_to_file(output_file, dictionary)
        sys.exit()
    else:
        key = word_input[0].upper()
        word_input = word_input.strip().lower()

        if key in dictionary:
            dictionary[key].append(word_input)
        else:
            dictionary[key] = []
            dictionary[key].append(word_input)
