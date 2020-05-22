"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project One
"""


def calculate_meters(inches: int) -> float:
    inches_to_centimeters = (lambda inches: inches * 2.54)
    centimeters_to_meters = (lambda centimeters: centimeters / 100)
    return (centimeters_to_meters(inches_to_centimeters(inches)))


def main():
    height_input_feet = input('Feet: ')
    height_input_inches = input('Inches: ')
    height_str = f"{height_input_feet}'{height_input_inches}\""
    output_str = ""

    feet = int(height_input_feet)
    inches = int(height_input_inches)
    inches_total = (feet * 12) + inches

    if inches_total <= 95:
        meters = calculate_meters(inches_total)
        output_str = f"Original Height Input {height_str} -> Converted to meters {meters:.2f}m"
    else:
        output_str = "Wow, you're so tall!"

    print(output_str)


if __name__ == "__main__":
    main()
