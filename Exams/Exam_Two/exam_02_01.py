def calculate_average(decimal_numbers: list) -> float:
    result = 0.0
    try:
        result = sum(
            decimal_numbers) / len(decimal_numbers)
    except ZeroDivisionError:
        print('Could not calculate average')

    return round(result, 2)


decimal_numbers: list = []

while True:
    try:
        number_input = float(input("Give me a number: "))
    except ValueError:
        print("Double check the value you entered or type '0' to exit")
    else:
        if number_input != 0:
            decimal_numbers.append(number_input)
        else:
            print('Sum of all numbers: ', sum(decimal_numbers))
            print('The average of all numbers: ',
                  calculate_average(decimal_numbers))
            break
