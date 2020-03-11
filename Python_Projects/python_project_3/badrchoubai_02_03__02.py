'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Three
'''


def display_results(results: list) -> None:
    '''display_results
    This function takes a list of results and prints them in a 
    prettified manner. 
    '''
    pass


def get_results(numbers: [int]) -> dict:
    '''calculate_results
    This method takes a list of integers and outputs per the problem specifications
    - All numbers that are below to the calculated average.
    - All numbers that equal to the calculated average. 
    - All numbers that are above to the calculated average.
    '''
    pass


numbers = []
while True:
    number_input = input("Give me a number: ")

    # validate input
    if number_input.isdigit() and number_input != '0':
        # append number_input to numbers list
        continue
    elif not number_input.isdigit():
        # Prompt user to enter a number
        continue
    else:
        # calculate and display results
        break
