import unittest
from projectone_01 import is_valid_letter_grade 
import random


class TestProblemOne(unittest.TestCase):

    """Test for is_valid_letter_grade method"""

    def test_is_valid_letter_grade(self):
        letter_grades = ['A+', 'B-', 'C'] + ['+A', 'HEY', 'Q-']
        counter = {"Valid": 0, "Invalid": 0}
        for lg in letter_grades:
            if is_valid_letter_grade(lg):
                counter["Valid"] += 1
            else:
                counter["Invalid"] += 1

        assert counter["Valid"] == counter["Invalid"]


if __name__ == "__main__":
    unittest.main()
