from string import ascii_uppercase


def update_letter_counts(sentence: list, char_occurences: dict) -> dict:
    for char in sentence:
        char_occurences[char] += 1

    return char_occurences


def main():
    char_occurences = dict(
        zip(ascii_uppercase, [0 for i in range(26)]))
    input_file = 'test sentences.txt'

    with open(input_file, 'r') as sentence_file:
        for line in sentence_file.readlines():
            if not line.isspace():
                line = line.replace('\n', '')
                line = line.upper()
                update_letter_counts(
                    [char for char in line if char.isalpha()], char_occurences)

    # Work on output display and file output


if __name__ == "__main__":
    main()
