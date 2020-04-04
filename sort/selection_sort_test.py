import unittest
import selection_sort

class TestFindSmallest(unittest.TestCase):

    def test_find_smallest_positive_sorted(self):
        arr = [1, 2, 3, 4, 5]
        res = selection_sort.find_smallest(arr)
        expected = 0
        self.assertEqual(res, expected)

    def test_find_smallest_positive_mixed(self):
        arr = [5, 3, 10, 55, 1, 0, 12, 999]
        res = selection_sort.find_smallest(arr)
        expected = 5
        self.assertEqual(res, expected)

    def test_find_smallest_negative_sorted(self):
        arr = [-1, -2, -3, -4, -5]
        res = selection_sort.find_smallest(arr)
        expected = 4
        self.assertEqual(res, expected)

    def test_find_smallest_negative_mixed(self):
        arr = [-12, -5, -99, -8729, -8728, -8730, -1, -5000, -10]
        res = selection_sort.find_smallest(arr)
        expected = 5
        self.assertEqual(res, expected)

    def test_find_smallest_mixed(self):
        arr = [-12, 10, -5, 0, -99, 555, 556, -8729, 32, 37, -8728, 8473620, -8730, -1, -5000, -10]
        res = selection_sort.find_smallest(arr)
        expected = 12
        self.assertEqual(res, expected)

    def test_find_smallest_mixed_repeated(self):
        arr = [-12, 10, -5, 0, 0, 0, -99, 555, 556, 555, -8729, 32, 37, -8728, 8473620, -8730, -8730, -1, 0, -5000, -10]
        res = selection_sort.find_smallest(arr)
        expected = 15
        self.assertEqual(res, expected)

    def test_find_smallest_repeated(self):
        arr = [0, 0, 0, 0, 0, 0]
        res = selection_sort.find_smallest(arr)
        expected = 0
        self.assertEqual(res, expected)

class TestSelectionSort(unittest.TestCase):

    def test_sort_positive_sorted(self):
        arr = [1, 2, 3, 4, 5]
        res = selection_sort.sort(arr)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(res, expected)

    def test_sort_positive_mixed(self):
        arr = [5, 3, 10, 55, 1, 0, 12, 999]
        res = selection_sort.sort(arr)
        expected = [0, 1, 3, 5, 10, 12, 55, 999]
        self.assertEqual(res, expected)

    def test_sort_negative_sorted(self):
        arr = [-1, -2, -3, -4, -5]
        res = selection_sort.sort(arr)
        expected = [-5, -4, -3, -2, -1]
        self.assertEqual(res, expected)

    def test_sort_negative_mixed(self):
        arr = [-12, -5, -99, -8729, -8728, -8730, -1, -5000, -10]
        res = selection_sort.sort(arr)
        expected = [-8730, -8729, -8728, -5000, -99, -12, -10, -5, -1]
        self.assertEqual(res, expected)

    def test_sort_mixed(self):
        arr = [-12, 10, -5, 0, -99, 555, 556, -8729, 32, 37, -8728, 8473620, -8730, -1, -5000, -10]
        res = selection_sort.sort(arr)
        expected = [-8730, -8729, -8728, -5000, -99, -12, -10, -5, -1, 0, 10, 32, 37, 555, 556, 8473620]
        self.assertEqual(res, expected)

    def test_sort_mixed_repeated(self):
        arr = [-12, 10, -5, 0, 0, 0, -99, 555, 556, 555, -8729, 32, 37, -8728, 8473620, -8730, -8730, -1, 0, -5000, -10]
        res = selection_sort.sort(arr)
        expected = [-8730, -8730, -8729, -8728, -5000, -99, -12, -10, -5, -1, 0, 0, 0, 0, 10, 32, 37, 555, 555, 556, 8473620]
        self.assertEqual(res, expected)

    def test_sort_repeated(self):
        arr = [0, 0, 0, 0, 0, 0]
        res = selection_sort.sort(arr)
        expected = [0, 0, 0, 0, 0, 0]
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()