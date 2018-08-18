import unittest
import problem001

class TestStringMethods(unittest.TestCase):
    def test_correct_up_to_10(self):
        self.assertEqual(problem001.sumOfMultiplesOf3and5(10), 23)

if __name__ == '__main__':
    unittest.main()
