'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Three

Part of the specifications states to allow for the possibility that there are no numbers below 
the average and/or no numbers above the average. so a question asked is. 

What does that mean about the numbers in the list?
'''


def display_results(results: tuple) -> None:
    '''display_results
    This function takes a list of results and prints them in a 
    prettified manner. 
    '''
    above_average, equal_to_average, below_average = results[0].values()
    calculated_average = results[1]
    print(f'''
    Calculated Average -> { calculated_average }
    Numbers above calculated average -> { above_average }
    Numbers equal to the calculated average -> { equal_to_average }
    Numbers below calculated average -> { below_average }
    ''')


def get_results(numbers: [int]) -> tuple:
    '''calculate_results
    This method takes a list of integers and outputs per the problem specifications
    - All numbers that are above the calculated average.
    - All numbers that equal the calculated average. 
    - All numbers that are below the calculated average.
    '''
    results = {
        'above_average': [],
        'equal_to_average': [],
        'below_average': [],
    }
    calculated_average = sum(numbers) / len(numbers)
    for number in numbers:
        if number > calculated_average:
            results['above_average'].append(number)
        elif number == calculated_average:
            results['equal_to_average'].append(number)
        elif number < calculated_average:
            results['below_average'].append(number)

    return (results, calculated_average)


numbers = []
while True:
    number_input = input("Give me a number: ")

    # validate input
    if number_input.isdigit() and number_input != '0':
        # append number_input to numbers list
        numbers.append(int(number_input))
        continue
    elif not number_input.isdigit():
        # Prompt user to enter a number
        print("Please enter a number.")
        continue
    else:
        # calculate and display results
        display_results(get_results(numbers))
        break
