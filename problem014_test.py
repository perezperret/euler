import unittest
import problem014

class TestStringMethods(unittest.TestCase):
    def test_collatz_length_of_10(self):
        self.assertEqual(problem014.collatz_length(13), 10)

if __name__ == '__main__':
    unittest.main()
