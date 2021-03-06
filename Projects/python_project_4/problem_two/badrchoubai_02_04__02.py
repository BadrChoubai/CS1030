from string import ascii_uppercase


def update_char_occurences(characters: list, char_occurences: dict) -> dict:
    for char in characters:
        char_occurences[char] += 1

    return char_occurences


def main():
    # Create a dictionary with characters A-Z; set values to 0;
    char_occurences = dict(
        zip(ascii_uppercase, [0 for i in range(26)]))

    input_file = '1030 Project 04 02 Sentences.txt'
    output_file = 'BadrChoubai 03 04 02 Output.txt'

    # Open the input file
    with open(input_file, mode='r') as sentence_file:
        # Parse each line in file
        for line in sentence_file.readlines():
            if line != '\n':
                update_char_occurences(
                    [char.upper() for char in line if char.isalpha()], char_occurences)

    # Display results in console and write them to file.
    with open(output_file, mode='w') as output_file:
        output_file.write('Letter -> Occurences\n')
        print('Letter -> Occurences')
        for char, char_occurence in char_occurences.items():
            output_file.write(f'{char} -> {char_occurence}\n')
            print(f'{char} -> {char_occurence}')


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as error:
        print(error)
