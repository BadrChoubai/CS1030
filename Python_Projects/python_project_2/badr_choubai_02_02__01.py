"""
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Two
"""
from re import match


def calculate_points(grade_input_stream: list, scores: dict) -> int:
    """
    Args:
        grade_input_stream: user input grades
        scores: scores to match grades against
    Returns:
        points: All points after calculation
    """
    points = 0

    for lg in grade_input_stream:
        points += scores[lg]

    return points


def is_valid_letter_grade(letter_grade: str) -> bool:
    """
    Args:
        letter_grade: letter grade input from user
    Returns:
        True if letter_grade in letter_score
        False if not letter_grade in letter_score
    """
    letter_grades = {'A', 'B', 'C', 'D', 'F',
                     'A+', 'A-', 'B+', 'B-', 'C+', 'C-', 'D+'}
    return letter_grade in letter_grades


scores = {
    'A+': 4.2, 'A': 4.0, 'A-': 3.9,
    'B+': 3.7, 'B': 3.2, 'B-': 3.0,
    'C+': 2.8, 'C': 2.2, 'C-': 2.0,
    'D+': 1.8, 'D': 1.2, 'F': 0,
}


def main():
    grades_processed = 0
    total_points = 0
    grade_input_stream: list = []

    while True:
        grade_input = input("Give me a letter grade: ")

        if grade_input == 'quit':
            print('Calculating GPA for all entries')
            overall_gpa = total_points / grades_processed
            print(f'Overall GPA: {overall_gpa:.2f}')
            break
        elif grade_input == '':
            print('Calculating GPA for latest entry...')
            points = calculate_points(grade_input_stream, scores)
            if points == 0:
                print("No GPA calculated.")
            else:
                print(f"Points in current entry: {points:.2f}")
                grades_processed += 1
                total_points += points
                grade_input_stream.clear()
            continue
        else:
            if is_valid_letter_grade(grade_input):
                grade_input_stream.append(grade_input)
            else:
                print("Please input a valid letter grade.")


if __name__ == "__main__":
    main()
