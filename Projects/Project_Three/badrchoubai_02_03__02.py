'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Three
'''


from typing import List


def calculate_results(numbers: List[int]) -> tuple:
    '''calculate_results
    This method takes a list of integers and outputs per the problem specifications
    - All numbers that are above the calculated average.
    - All numbers that equal the calculated average.
    - All numbers that are below the calculated average.
    '''
    calculated_average = 0
    results = {
        'above_average': [],
        'equal_to_average': [],
        'below_average': [],
    }

    try:
        calculated_average = sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print('No Average Calculated')
    else:
        for number in numbers:
            if number > calculated_average:
                results['above_average'].append(number)
            if number == calculated_average:
                results['equal_to_average'].append(number)
            if number < calculated_average:
                results['below_average'].append(number)

    return (calculated_average, results)


def display_results(results: tuple) -> None:
    '''display_results
    This function takes a results tuple with two values and prints them.
    '''
    calculated_average = round(results[0], 2)
    above_average, equal_to_average, below_average = results[1].values()
    print(f'''
    Calculated Average -> {calculated_average or None}
    Numbers above calculated average -> {', '.join(str(n) for n in above_average) or None}
    Numbers equal to the calculated average -> {', '.join(str(n) for n in equal_to_average) or None}
    Numbers below calculated average -> {', '.join(str(n) for n in below_average) or None}
    ''')


def main():
    numbers = []
    while True:
        number_input = input("Give me a number: ")

        # validate input
        if number_input.isdigit() and number_input != '0':
            # append number_input to numbers list
            numbers.append(int(number_input))
        elif not number_input.isdigit():
            # Prompt user to enter a number
            print("Please enter a number.")
            continue
        else:
            # calculate and display results
            calculated_results = calculate_results(numbers)
            display_results(calculated_results)
            break


if __name__ == "__main__":
    main()
