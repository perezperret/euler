import unittest
import problem006

class TestStringMethods(unittest.TestCase):
    def test_square_sum_of_4(self):
        self.assertEqual(problem006._squareSum(4), 30)

    def test_correct_for_10(self):
        self.assertEqual(problem006.sumSquareDifference(10), 2640)

if __name__ == '__main__':
    unittest.main()
