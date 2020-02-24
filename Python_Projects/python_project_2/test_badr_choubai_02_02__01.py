"""
    1.1 Loop until the user enters ‘quit’ at which time proceed at step 1.6.

    1.2 Do an inner loop until the user enters a blank line.

    1.3 Prompt the user for the next grade. If the grade is invalid (e.g., E+, +A, G, HEY, or Q-), ignore this grade, inform the user and prompt again.

    1.4 Here, the user entered a valid grade. Using a list or a series of if-elif-else statements, translate the grade to points and accumulate the total points and the count so you can calculate an overall average later. Prompt for the next grade.

    1.5 If the user enters a blank line, calculate and print the GPA for the grades just entered. Your program should correctly handle the case where the user enters no grades. In that case, print “No GPA calculated” and resume at step 1.2.

    1.6 Calculate and print the overall average of all GPAs that were processed.
"""

import unittest
import badr_choubai_02_02__01 as problem_one
import random


class TestProblemOne(unittest.TestCase):

    """Test for is_valid_letter_grade method"""

    def test_is_valid_letter_grade(self):
        letter_grades = ['A+', 'B-', 'C'] + ['+A', 'HEY', 'Q-']
        counter = {"Valid": 0, "Invalid": 0}
        for lg in letter_grades:
            if problem_one.is_valid_letter_grade(lg):
                counter["Valid"] += 1
            else:
                counter["Invalid"] += 1

        assert counter["Valid"] == counter["Invalid"]


if __name__ == "__main__":
    unittest.main()
