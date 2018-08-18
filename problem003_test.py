import unittest
import problem003

class TestStringMethods(unittest.TestCase):
    def test_divide_while_divisor_21_7(self):
        self.assertEqual(problem003._divideWhileDivisor(21, 7), 3)

    def test_divide_while_divisor_18_3(self):
        self.assertEqual(problem003._divideWhileDivisor(18, 3), 2)

    def test_correct_for_35(self):
        self.assertEqual(problem003.maxPrimeDiv(35), 7)

    def test_correct_for_289(self):
        self.assertEqual(problem003.maxPrimeDiv(289), 17)


if __name__ == '__main__':
    unittest.main()
