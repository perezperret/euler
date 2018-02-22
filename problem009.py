'''
  Problem: find product of pythagorean triple where a + b + c === 1000
'''
from operator import mul
from functools import reduce
import math

'''
  Find pythagorean triple using euclid's formula
'''
def _findPythagoreanTriple(m, n, k = 1):
  if (not (m > n)): return

  a = k * int(math.pow(m, 2) - math.pow(n, 2))
  b = k * int(2 * m * n)
  c = k * int(math.pow(m, 2) + math.pow(n, 2))

  return (a, b, c);

a, b, c = _findPythagoreanTriple(2, 1, 1)

assert math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)

'''
  Iterate through all pythagorean triples below a given number and test if the
  sum of its items is a factor of the given number
  Returns a pythagorean triple that sums the given number 
'''
def findPythTripleWithSum(total):
  m = 2
  result = 0
  while (result < total):
    for n in range(1, m - 1):
      result = sum(_findPythagoreanTriple(m, n))
      if (result == total):
        return  _findPythagoreanTriple(m, n)
      elif (total % result == 0):
        return _findPythagoreanTriple(m, n, total // result)
    m += 1

assert findPythTripleWithSum(440) == (40, 198, 202)

print(reduce(mul, findPythTripleWithSum(1000)))
