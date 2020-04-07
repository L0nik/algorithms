import unittest
import quick_sort

class QuickSortTest(unittest.TestCase):

    def test_normal(self):
        arr = [5, 7, 0, -2, 1]
        expected = [-2, 0, 1, 5, 7]
        res = quick_sort.qsort(arr)
        self.assertEqual(res, expected)

    def test_empty(self):
        arr = []
        expected = []
        res = quick_sort.qsort(arr)
        self.assertEqual(res, expected)

    def test_sorted_asc(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        res = quick_sort.qsort(arr)
        self.assertEqual(res, expected)

    def test_sorted_desc(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        res = quick_sort.qsort(arr)
        self.assertEqual(res, expected)

    def test_zeros(self):
        arr = [0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0]
        res = quick_sort.qsort(arr)
        self.assertEqual(res, expected)

    def test_negative(self):
        arr = [-5, -5, -7, -3, -1]
        expected = [-7, -5, -5, -3, -1]
        res = quick_sort.qsort(arr)
        self.assertEqual(res, expected)

    def test_mixed(self):
        arr = [5, -5, 0, -3, -1, 0, 10, -10, 7]
        expected = [-10, -5, -3, -1, 0, 0, 5, 7, 10]
        res = quick_sort.qsort(arr)
        self.assertEqual(res, expected)

    
if __name__ == '__main__':
    unittest.main()
