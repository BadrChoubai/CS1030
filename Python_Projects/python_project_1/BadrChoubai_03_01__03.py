"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030

### Description ###

This is my solution for problem three of three of Python Project One

The Problem:

    Print the color of a square on a chessboard.

    # 3.1 Print a multi-line message explaining what the program does and the format of the input.

    # 3.2 Prompt the user to enter two characters, the first one a letter, the second one a digit. Examples of input are given above.

    # 3.3 Ensure the first character is in the range of a-h and the second one is in the range of 1-8. If not print an error message and exit the program.

    # 3.4 From the letter and digit combination determine the color of the square and print the result to the user with a message like “Square e4 is white” or “Square d6 is black.”

    # 3.5 Test your program with invalid squares like j5 or a9.

    # 3.6 Exit the program.

"""


def get_user_input(prompts: list) -> list:
    prompt_answers: list  = [] 

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

    letter_range = list(map(chr, range(97, 105)))
    number_range = [i for i in range(1, 9)]

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

