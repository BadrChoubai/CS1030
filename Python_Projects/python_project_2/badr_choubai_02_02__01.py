'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Two
'''


def calculate_gpa(scores: [float]) -> float:
    '''
    Args:
        scores: all scores accumulated during input
    Returns:
        calculated GPA or None
    '''
    return round(sum(scores) / len(scores), 2) if len(scores) > 0 else 0


def is_valid_letter_grade(letter_grade: str) -> bool:
    '''
    Args:
        letter_grade: letter grade received from user input
    Returns:
        boolean value for letter_grade in set of valid letter grades
    '''
    return letter_grade in {'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F'}


def score_for_letter_grade(letter_grade: str) -> float:
    '''
    Args:
        letter_grade: letter grade received from user input
    Returns:
        Points value for passed in letter_grade
    '''
    return {
        'A': 4.0, 'A-': 3.9, 'A+': 4.2,
        'B': 3.2, 'B-': 3.0, 'B+': 3.7,
        'C': 2.2, 'C-': 2.0, 'C+': 2.8,
        'D+': 1.8, 'D': 1.2, 'F': 0
    }[letter_grade]


def main():
    all_scores = []
    series_scores = []

    while True:
        grade_input = input("Enter a letter grade: ")

        if is_valid_letter_grade(grade_input):
            series_scores.append(score_for_letter_grade(grade_input))
        elif grade_input == 'quit':
            all_scores += series_scores
            overall_gpa = calculate_gpa(all_scores)
            print(f'Overall GPA: { overall_gpa }') if overall_gpa > 0 else print(
                'No GPA calculated')
            break
        elif grade_input == '':
            latest_gpa = calculate_gpa(series_scores)
            all_scores += series_scores
            print(f'GPA for latest entries { latest_gpa }') if latest_gpa > 0 else print(
                'No GPA calculated')
        else:
            print("Please enter a valid letter grade.")


if __name__ == "__main__":
    main()
