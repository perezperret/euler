'''
  Problem: find sum of primes up to 2 million
'''
import math
## from prob 7
def _removeMults(divider, nums):
  start = nums.index(int(math.pow(divider, 2)))
  print(divider, '...')
  for index, num in enumerate(nums[start:]):
    if (num % divider == 0):
      nums[start + index] = None
  nums = list(filter(None, nums))
  return nums
      
'''
  Sum of 'Sieve of Eratosthenes'
'''
def sumPrimes(limit):
  result = 2
  odds = list(range(3, limit, 2))
  while (len(odds) > 0):
    prime = odds.pop(0)
    result += prime
    if (len(odds) > 0 and math.pow(prime, 2) <= odds[-1]):
      odds = _removeMults(prime, odds)
    # print('sum: ' + str(result) + '. len: ' + str(len(odds)) + '. current: ' + str(prime))

  return result

assert sumPrimes(10) == 17

print(sumPrimes(2000000))