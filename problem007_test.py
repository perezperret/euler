import unittest
import problem007

class TestStringMethods(unittest.TestCase):
    def test_remove_mults(self):
        self.assertEqual(problem007._removeMults(2, list(range(3, 11))), list(range(3, 11, 2)))

    def test_find_primes(self):
        self.assertEqual(problem007._findPrimes(list(range(2, 11))), [2, 3, 5, 7])

    def test_find_7th_prime(self):
        self.assertEqual(problem007.nthPrime(7), 17)

    def test_find_8th_prime(self):
        self.assertEqual(problem007.nthPrime(8), 19)

    def test_find_9th_prime(self):
        self.assertEqual(problem007.nthPrime(9), 23)

    def test_find_10th_prime(self):
        self.assertEqual(problem007.nthPrime(10), 29)

if __name__ == '__main__':
    unittest.main()
