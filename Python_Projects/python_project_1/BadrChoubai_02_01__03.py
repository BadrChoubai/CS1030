"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project One
"""


def find_color(coordinate: tuple) -> str:
    coordinate = ord(coordinate[0]) + int(coordinate[1])
    return "Black" if coordinate % 2 == 0 else "Red"


def is_valid_coordinate(coordinate: tuple) -> bool:
    coordinate_letter = coordinate[0] if coordinate[0].isalpha() else None
    coordinate_number = coordinate[1] if coordinate[1].isdigit() else None

    return [coordinate_letter, coordinate_number]


def in_range(coordinate: tuple) -> bool:
    letter_range = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    number_range = [1, 2, 3, 4, 5, 6, 7, 8]

    return coordinate[0] in letter_range and int(coordinate[1]) in number_range


def print_intro():
    intro_message = str("""
    Welcome to Checkerboard Color Guess!

    This program does two things

        1. Takes your input for a location on a checkerboard
            Ex. Letter: a(-h), Number: 1(-8)

        2. Outputs the color of the color of said square on the checkboard
            Ex. Square a8 is white
    """)

    print(intro_message)


def main():
    print_intro()

    coordinate = input("Give me a coordinate (a-h)(1-8) -> ")
    coordinate = (coordinate[0], coordinate[1])

    letter, number = is_valid_coordinate(coordinate)
    if letter and number and in_range(coordinate):
        color = find_color(coordinate)
        print(f"Square { letter }{ number } is { color }")
    else:
        print("Double check that you input a valid coordinate.")


if __name__ == "__main__":
    main()
