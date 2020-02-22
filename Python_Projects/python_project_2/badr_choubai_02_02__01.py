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


"""
This method uses regex to match correctly input letter grades,
"""


def is_valid_letter_grade(letter_grade: str) -> bool:
    valid_grade_re = r'^[A-D][-+]?$'
    return match(valid_grade_re, letter_grade)


"""
This method will update the counter of the letter grade the user input 
"""


def update_grade_book(grade_book: dict, letter_grade: str) -> dict:
    grade_book[letter_grade][0] += 1
    return grade_book


""" 
This dict represents a dict where the keys, represented by letter grades have a tuple value
The tuple's left side represents how many of that Letter grade the user input
The tuple's right side represent how many point that letter grade is worth

grade_book: dict(str, list(int, float))
"""
grade_book = {
    'A+': [0, 4.2], 'A': [0, 4.0], 'A-': [0, 3.9],
    'B+': [0, 3.7], 'B': [0, 3.2], 'B-': [0, 3.0],
    'C+': [0, 2.8], 'C': [0, 2.2], 'C-': [0, 2.0],
    'D+': [0, 1.8], 'D': [0, 1.2],
}


def main():
    while True:
        grade_input = input("Please enter a letter grade: ")
        if grade_input == '' or grade_input == 'quit':
            print(grade_book)
            break
        else:
            if is_valid_letter_grade(grade_input):
                update_grade_book(grade_book, grade_input)
            else:
                print("Enter a valid letter grade. F is ignored.")


if __name__ == "__main__":
    main()
