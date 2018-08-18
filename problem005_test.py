import unittest
import problem005

class TestStringMethods(unittest.TestCase):
    def test_correct_for_10(self):
        self.assertEqual(problem005.compactFactorial(10), 2520)

    def test_correct_for_20(self):
        self.assertEqual(problem005.compactFactorial(20), 232792560)

if __name__ == '__main__':
    unittest.main()
