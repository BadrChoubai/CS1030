import unittest
from badrchoubai_02_03__03 import search_provinces, is_valid_postal_code


class TestProblemThree(unittest.TestCase):

    def test_search_provinces(self):
        # for T2N 1N4, your program should display that the address is an urban one in Alberta
        self.assertEqual(search_provinces('T2N 1N4'), (['alberta'], 'Urban'))
        # for X0A 1B2, your program should display that the address is a rural one in Nunavut or Northwest Territories
        self.assertEqual(search_provinces('X0A 1B2'),
                         (['nunavut or the northwest_territories'], 'Rural'))
        self.assertEqual(search_provinces('R8N 1R7'), (['manitoba'], 'Urban'))
        self.assertEqual(search_provinces('V5K 7V5'),
                         (['british_columbia'], 'Urban'))
        self.assertEqual(search_provinces('J0J 5S6'),
                         (['quebec'], 'Rural'))

    def test_is_valid_postal_code(self):
        self.assertEqual(is_valid_postal_code('T2N 1N4'), True)
        self.assertEqual(is_valid_postal_code('X0A 1B2'), True)
        self.assertEqual(is_valid_postal_code('K1A0B1'), False)
        # if postal code starts with one of these letters it will be invalid
        # {'D', 'F', 'I', 'O', 'Q', 'U', 'W', 'Z'}
        self.assertEqual(is_valid_postal_code('Z0A 5B4'), False)


if __name__ == '__main__':
    unittest.main()
