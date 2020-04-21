def letter_score(letter: str) -> int:
    return {
        'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }[letter]


def main():
    all_words = []
    input_file = '1030 Project 04 01 Words.txt'

    with open(input_file, 'r') as word_submissions:
        for line in word_submissions.readlines():
            if not line.isspace():
                word = line.replace('\n', '').upper()
                all_words.append(word)

    scores = [sum([letter_score(letter) for letter in word])
              for word in all_words if word.isalpha()]

    print('Word -> Score')
    for word, score in zip(all_words, scores):
        print(word, score)


if __name__ == "__main__":
    main()
