"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project One
"""


def feet_to_inches(feet: int) -> int:
    return (feet * 12)


def centimeters_to_meters(centimeters: float) -> float:
    return (centimeters / 100)


def calculate_meters(inches: int) -> float:
    return (centimeters_to_meters(inches_to_centimeters(inches)))


def inches_to_centimeters(inches: int) -> float:
    return (inches * 2.54)


def main():

    height = input("Input you height as feet'inches\": ")
    height = height.replace('\'', ' ').replace('"', '')

    (feet, inches) = height.split(' ')
    feet = int(feet)
    inches = int(inches)

    inches_total = feet_to_inches(feet) + inches
    meters = calculate_meters(inches_total)

    height_str = f"{feet}'-{inches}\""
    output_str = f"Original Height Input {height_str} -> Converted to meters {meters:.2f}m"

    print(output_str) if inches_total <= 95 else print("Wow, you're so tall!")


if __name__ == "__main__":
    main()
