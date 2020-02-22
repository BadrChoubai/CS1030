"""
    # 1.1 Loop until the user enters ‘quit’ at which time proceed at step 1.6.
 
    # 1.2 Do an inner loop until the user enters a blank line.

    # 1.3 Prompt the user for the next grade. If the grade is invalid (e.g., E+, +A, G, HEY, or Q-), ignore this grade, inform the user and prompt again.

    1.4 Here, the user entered a valid grade. Using a list or a series of if-elif-else statements, translate the grade to points and accumulate the total points and the count so you can calculate an overall average later. Prompt for the next grade.

    1.5 If the user enters a blank line, calculate and print the GPA for the grades just entered. Your program should correctly handle the case where the user enters no grades. In that case, print “No GPA calculated” and resume at step 1.2.

    1.6 Calculate and print the overall average of all GPAs that were processed. 
        - Overall Average = Sum of all points / Number of grades preocessed

    Regex Pattern for letter Grade
    https://regex101.com/r/uvsEdU/3
"""
from re import match


"""is_valid_letter_grade
This method implements a regex pattern to check that the letter grade input by the user is valid
"""


def is_valid_letter_grade(letter_grade: str) -> bool:
    valid_grade_re = r'^[A-D][-+]?$'
    return match(valid_grade_re, letter_grade)


scores = {
    'A+': 4.2, 'A': 4.0, 'A-': 3.9,
    'B+': 3.7, 'B': 3.2, 'B-': 3.0,
    'C+': 2.8, 'C': 2.2, 'C-': 2.0,
    'D+': 1.8, 'D': 1.2,
}

score_counter = {
    'A+': 0, 'A': 0, 'A-': 0,
    'B+': 0, 'B': 0, 'B-': 0,
    'C+': 0, 'C': 0, 'C-': 0,
    'D+': 0, 'D': 0,
}


def main():
    while True:
        grade_input = input("Give me a letter grade: ")

        if grade_input == 'quit':
            print('Quit')
            break
        elif grade_input == '':
            print('no input')
            continue
        else:
            if is_valid_letter_grade(grade_input):
                score_counter[grade_input] += 1
            else:
                print("Please input a valid letter grade. Fs are ignored")


if __name__ == "__main__":
    main()
