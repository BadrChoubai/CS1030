import unittest
from unittest.mock import patch

import badrchoubai_03_01__01 as problem_one


class TestProblemOne(unittest.TestCase):

    def test_feet_to_inches(self):
        actual = problem_one.feet_to_inches(5)
        expected = 60

        self.assertEqual(actual, expected)

    def test_centimeters_to_meters(self):
        actual = problem_one.centimeters_to_meters(10.16)
        expected = 0.1016

        self.assertEqual(actual, expected)

    def test_calculate_meters(self):
        actual = problem_one.calculate_meters(64)
        expected = 1.6256

        self.assertEqual(actual, expected)

    def test_get_user_input(self):
        prompts: list = ['Question One', 'Question Two'] 

        with patch('builtins.input') as mock_get_user_input:
            mock_get_user_input.side_effect = ['1', '2']
            result = problem_one.get_user_input(prompts)
            assert result == [1, 2]
            assert len(result) == len(prompts)
        
    def test_inches_to_centimeters(self):
        actual = problem_one.inches_to_centimeters(64)
        expected = 162.56

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

"""
    from unittest.mock import patch
    
    with patch('__main__.input') as mock_input:
        mock_input.side_effect = ['1','2','3']
        result = get_user_input(['one','two','three'])
        assert result == [3,4,5]
"""
