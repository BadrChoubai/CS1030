words = []

while True:
    word = input('Type in a word: ')
    if word == '':
        break
    else:
        words.append(word)
        if len(words) == 1:
            print(words[0])
        else:
            print('%s and %s' % (', '.join(words[:-1]), words[-1]))
