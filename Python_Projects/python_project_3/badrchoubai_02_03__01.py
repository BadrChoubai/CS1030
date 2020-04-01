'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Three
'''


def convert(degrees_celsius: int) -> float:
    '''convert
    This method takes a temperature value in celsius and converts it to fahrenheit
    '''
    return (1.8) * (degrees_celsius) + 32


print(f'| Celsius | Fahrenheit |')
print(f'|---------|------------|')
for i in range(0, 101, 10):
    celsius, fahrenheit = i, convert(i)
    print(f'| {celsius}{" "*(7 - len(str(celsius)))} | {fahrenheit:.0f}{" "*(12 - len(str(fahrenheit)))} |')
