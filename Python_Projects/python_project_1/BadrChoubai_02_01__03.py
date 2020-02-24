"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project One
"""


def get_user_input(prompts: list) -> list:
    prompt_answers: list = []

    for prompt_message in prompts:
        answer = input(f"{ prompt_message }: ")
        prompt_answers.append(answer.strip())

    return prompt_answers


def find_color(letter, number):
    coordinate = ord(letter) + int(number)

    if coordinate % 2 == 0:
        return "Black"
    else:
        return "White"


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

    prompts: list = ["Give me a letter from a-h",
                     "Give me a number from 1-8"]

    [letter, number] = get_user_input(prompts)

    letter_range = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    number_range = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if letter in letter_range and int(number) in number_range:
        color = find_color(letter, number)
        output_str = f"Tile {letter}{number} is {color}"

        print(output_str)

    else:
        error = str(
            "Double check that the values you entered are in the correct range.")
        print(error)


if __name__ == "__main__":
    main()
