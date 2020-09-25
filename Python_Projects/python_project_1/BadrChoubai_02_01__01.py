"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project One
"""


def main():

    feet_to_inches = lambda feet: feet * 12
    centimeters_to_meters = lambda centimeters: centimeters / 100
    calculate_meters = lambda inches: centimeters_to_meters(inches_to_centimeters(inches))
    inches_to_centimeters = lambda inches: inches* 2.54

    feet = input("Enter your height in feet\n> ")
    inches = input("Inches?\n> ")

    feet = int(feet)
    inches = int(inches)

    inches_total = feet_to_inches(feet) + inches
    meters = calculate_meters(inches_total)

    height_str = f"{feet}'-{inches}\""
    output_str = f"Original Height Input {height_str} -> Converted to meters {meters:.2f}m"

    print(output_str) if inches_total <= 95 else print("Wow, you're so tall!")


if __name__ == "__main__":
    main()
