'''
result = 4 / 0
print(result) // ZeroDivisionError: division by zero
'''

print('Enter two numbers and I\'ll divide them.')

while True:
    first_number = input('First Number: ')
    second_number = input('Second Number: ')

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Division by Zero not allowed')
    except ValueError:
        print('Please enter a number value')
    else:
        print(answer)
