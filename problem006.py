'''
  Problem: find sum(e)**2 - sum(e**2) for E = [1-100]
'''
import math

def sumSquareDifference(limit):
  sumSquare = math.pow(sum(range(1, limit + 1)), 2)
  squareSum = _squareSum(limit)
  return int(sumSquare - squareSum)

def _squareSum(limit):
  result = i = 0
  while(i <= limit):
    result += math.pow(i, 2)
    i += 1
  return int(result)

assert _squareSum(4) == 30
assert sumSquareDifference(10) == 2640

print(sumSquareDifference(100))