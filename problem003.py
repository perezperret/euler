'''
  Problem: largest prime factor of 600851475143
'''
import math

problemNum = 600851475143;

def maxPrimeDiv(num):
  if(num % 2 == 0):
    num = _divideWhileDivisor(int(num / 2), 2)
  possible = 3
  while(possible < num / 2):
    if(num % possible == 0):
      num = _divideWhileDivisor(int(num / possible), possible)
      possible = 3
    possible += 2
  return num

'''
  Divide num while divisor is a factor num / divisor
  Return smallest divided integer
'''
def _divideWhileDivisor(num, divisor):
  while(num != divisor and num % divisor == 0):
    num /= divisor
  return num

assert _divideWhileDivisor(21, 7) == 3
assert _divideWhileDivisor(18, 3) == 2

assert maxPrimeDiv(35) == 7;
assert maxPrimeDiv(289) == 17;

print(maxPrimeDiv(problemNum))