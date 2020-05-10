"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project One
"""
import sys


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

    coordinate = input('Input a coordinate as a(-h)1(-8) Ex. j3: ')
    in_range = coordinate[0] in "abcdefgh" and coordinate[1] in '12345678'

    if in_range:
        tile_color = "Black" if (
            ord(coordinate[0]) + int(coordinate[1])) % 2 == 0 else "White"

        print('Tile', coordinate, f'is {tile_color}')
    else:
        print('Coordinate input out of range.')
        sys.exit()


if __name__ == "__main__":
    main()
