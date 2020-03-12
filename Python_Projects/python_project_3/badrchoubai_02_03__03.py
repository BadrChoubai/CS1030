'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Three
'''


def is_valid_postal_code(postal_code_input: str) -> bool:
    '''is_valid_postal_code
    This method takes the postal code input and runs a series of checks to see whether
    or not it is a valid input.
    '''
    # if postal code starts with one of these letters it will be invalid
    invalid_letters = {'D', 'F', 'I', 'O', 'Q', 'U', 'W', 'Z'}
    valid_length = True if len(postal_code_input) == 7 else False
    valid_format = True if postal_code_input[3] == ' ' else False
    valid_letter = True if postal_code_input[0] not in invalid_letters else False

    return valid_length and valid_format and valid_letter


canadian_postal_codes = {
    'newfoundland': 'A',
    'nova_scotia': 'B',
    'prince_edward_island': 'C',
    'new_brunswick': 'E',
    'quebec': 'GHJ',
    'ontaria': 'KLMNP',
    'manitoba': 'R',
    'saskatchewan': 'S',
    'alberta': 'T',
    'british_columbia': 'V',
    'nunavut': 'X',
    'northwest_territories': 'X',
    'yukon': 'Y',
}


while True:
    postal_code_input = input("Enter a Canadian postal code: ")

    if postal_code_input == '':
        break
    elif is_valid_postal_code(postal_code_input):
        province_type = 'Rural' if postal_code_input[1] == '0' else 'Urban'

        letter = postal_code_input[0]
        for province, letters in canadian_postal_codes.items():
            if letter in letters:
                print(province, province_type) 

        continue
