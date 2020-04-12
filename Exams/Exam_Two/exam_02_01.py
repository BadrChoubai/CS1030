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
