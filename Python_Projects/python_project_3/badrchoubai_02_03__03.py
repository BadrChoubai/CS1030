'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Three
'''
import sys
import re


def print_search_results(results: tuple) -> None:
    '''print_search_results
    This method takes the results from the search_provinces method and pretty
    prints them.
    '''
    province_list, province_type = results
    for i, _ in enumerate(province_list):
        province_list[i] = province_list[i].replace('_', ' ').title()

    print(
        f'The postal code you entered is for a {province_type} in {province_list[0]}')


def is_valid_postal_code(postal_code_input: str) -> bool:
    '''is_valid_postal_code
    This method takes the postal code input and matches it to a regular expression.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s15.html
    '''
    postal_code_re = r'^(?!.*[DFIOQU])[A-VXY][0-9][A-Z] [0-9][A-Z][0-9]$'
    return True if re.compile(postal_code_re).match(postal_code_input) else False


def search_provinces(postal_code_input: str) -> tuple:
    '''search_provinces
    This method takes the province code input and returns a tuple containing
    the province type and the province that matches the province code
    '''
    canadian_provinces = {
        'newfoundland': 'A',
        'nova_scotia': 'B',
        'prince_edward_island': 'C',
        'new_brunswick': 'E',
        'quebec': 'GHJ',
        'ontario': 'KLMNP',
        'manitoba': 'R',
        'saskatchewan': 'S',
        'alberta': 'T',
        'british_columbia': 'V',
        'nunavut or the northwest_territories': 'X',
        'yukon': 'Y',
    }
    province_type = 'Rural' if postal_code_input[1] == '0' else 'Urban'
    province_list = []

    letter = postal_code_input[0]
    for province, letters in canadian_provinces.items():
        if letter in letters:
            province_list.append(province)

    return (province_list, province_type)


def main():
    while True:
        postal_code_input = input("Enter a Canadian postal code: ")

        if is_valid_postal_code(postal_code_input):
            search_results = search_provinces(postal_code_input)
            print_search_results(search_results)
            continue
        elif postal_code_input == '':
            sys.exit()
        else:
            print(
                f'Please enter a valid Canadian postal code')


if __name__ == '__main__':
    main()
