import unittest
import problem002

class TestStringMethods(unittest.TestCase):
    def test_fibs_up_to_25(self):
        self.assertEqual(problem002.fib(25), [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_sum_evens(self):
        self.assertEqual(problem002.sumEvens([0, 1, 1, 2, 3, 5, 8, 13, 21]), 10)

if __name__ == '__main__':
    unittest.main()
