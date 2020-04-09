'''
1.(10 points)Write a program that prompts repeatedly for decimal numbers. Store each number in a list. Stop asking for numbers when the user enters a 0 which is not stored in the list. Calculate and print two lines of output as follows: 

Line 1The sum of all the numbers: sum goes here 
Line 2The average of all the numbers: average goes here 

Example: for inputs of 10.5, 9.5, 8, -6.0 and 0, the four numbers are stored in a list and the program generates this output: 
 
The sum of all the numbers: 22.0 

The average of all the numbers: 5.5 
'''


def calculate_average(decimal_numbers: [float]) -> float:
    result = 0
    try:
        result = sum(
            decimal_numbers) / len(decimal_numbers)
    except ZeroDivisionError:
        print('Could not calculate average')
    else:
        return round(result, 2)


decimal_numbers: [float] = []
while True:
    number_input = input("Give me a number: ")

    try:
        number_input = float(number_input)
    except ValueError:
        print('Double check the value you entered')
    else:
        if number_input != 0:
            decimal_numbers.append(number_input)
        else:
            print('Sum of all numbers: ', sum(decimal_numbers))
            print('The average of all numbers: ',
                  calculate_average(decimal_numbers))
            break
