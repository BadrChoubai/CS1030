"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Two
"""
from functools import reduce
from re import match


def calculate_points(grade_input_stream: list, scores: dict) -> int:
    points = 0

    for lg in grade_input_stream:
        points += scores[lg]

    return points


def is_valid_letter_grade(letter_grade: str) -> bool:
    """is_valid_letter_grade
    This method implements a regex pattern to check that the letter grade input by the user is valid
    """
    valid_grade_re = r'^[A-D][-+]?$'
    return match(valid_grade_re, letter_grade)


scores = {
    'A+': 4.2, 'A': 4.0, 'A-': 3.9,
    'B+': 3.7, 'B': 3.2, 'B-': 3.0,
    'C+': 2.8, 'C': 2.2, 'C-': 2.0,
    'D+': 1.8, 'D': 1.2,
}

grade_input_stream: list = []


def main():
    grades_processed = 0
    total_points = 0

    while True:
        grade_input = input("Give me a letter grade: ")

        if grade_input == 'quit':
            print('Calculating GPA for all entries')
            print(f'Overall GPA: { total_points / grades_processed }')
            break
        elif grade_input == '':
            print('Calculating GPA for latest entry...')
            points = calculate_points(grade_input_stream, scores)
            if points == 0:
                print("No GPA calculated.")
            else:
                print(f"Points in current entry: {points}")
                grades_processed += 1
                total_points += points
                grade_input_stream.clear()
            continue
        else:
            if is_valid_letter_grade(grade_input):
                grade_input_stream.append(grade_input)
            else:
                print("Please input a valid letter grade. Fs are ignored")


if __name__ == "__main__":
    main()
