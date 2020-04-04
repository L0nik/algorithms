import unittest
import binary_search

class BinatySearchTest(unittest.TestCase):
    
    def test_binary_search_lboundary(self):
        result = binary_search.search([1, 2, 3, 4], 1)
        expected = 0
        self.assertEqual(result, expected)

    def test_binary_search_rboundary(self):
        result = binary_search.search([1, 2, 3, 4], 4)
        expected = 3
        self.assertEqual(result, expected)

    def test_binary_search_empty_list(self):
        result = binary_search.search([], 4)
        expected = None
        self.assertEqual(result, expected)

    def test_binary_search_value_present(self):
        result = binary_search.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5)
        expected = 4
        self.assertEqual(result, expected)

    def test_binary_search_value_absent(self):
        result = binary_search.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], -5)
        expected = None
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
