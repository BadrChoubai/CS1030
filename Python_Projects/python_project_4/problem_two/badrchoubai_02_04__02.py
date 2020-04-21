from string import ascii_uppercase


def update_char_occurences(characters: list, char_occurences: dict) -> dict:
    for char in characters:
        char_occurences[char] += 1

    return char_occurences


def main():
    # create dictionary with characters A-Z; set values to 0;
    char_occurences = dict(
        zip(ascii_uppercase, [0 for i in range(26)]))
    input_file = 'test sentences.txt'

    # Open the input file
    with open(input_file, 'r') as sentence_file:
        # parse and clean up each line in file
        for line in sentence_file.readlines():
            if not line.isspace():
                line = line.replace('\n', '')
                print(line)

                update_char_occurences(
                    [char.upper() for char in line if char.isalpha()], char_occurences)

    # Work on final output to console and to file


if __name__ == "__main__":
    main()
