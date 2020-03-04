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
        calculated GPA
    '''
    return round(sum(scores) / len(scores), 2)


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
    pass


if __name__ == "__main__":
    main()
