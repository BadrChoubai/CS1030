def update_letter_counts(sentence: list, letter_occurences: dict) -> dict:
    for letter in sentence:
        if letter in letter_occurences:
            letter_occurences[letter] += 1
        else:
            letter_occurences[letter] = 0
            letter_occurences[letter] += 1

    return letter_occurences


def main():
    letter_occurences = {}
    input_file = 'test sentences.txt'

    with open(input_file, 'r') as sentence_file:
        # Work on output display and file output
        for line in sentence_file.readlines():
            if not line.isspace():
                line = line.replace('\n', '')
                print(line)
                line = line.upper()
                update_letter_counts(
                    [c for c in line if c.isalpha()], letter_occurences)

    print(letter_occurences)


if __name__ == "__main__":
    main()
