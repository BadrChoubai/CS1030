import unittest

from dictionary_builder import dictionary_builder


class DictionaryBuilderTest(unittest.TestCase):

    def test_correctness(self):
        actual = dictionary_builder([('Subaru', ['Forester', 'Legacy'])])
        expected = {
            'Subaru': ['Forester', 'Legacy']
        }

        return self.assertEqual(actual, expected)

    def test_empty_list(self):
        actual = dictionary_builder([])
        expected = None

        return self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
