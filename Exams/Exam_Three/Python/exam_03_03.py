string = input('Give me a word or phrase: ')

characters_in_input = {}

for char in string:
    if char.isalpha():
        if char in characters_in_input:
            characters_in_input[char] += 1
        else:
            characters_in_input[char] = 1

unique_chars = len(characters_in_input.keys())

print(
    f'Unique characters -> {unique_chars}\nCharacter dictionary:\n{characters_in_input}')
