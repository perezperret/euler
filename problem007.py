'''
  Problem: find 10001th prime number
'''
import math
      
'''
  Removes all multiples of the given divider from the given list
  Returns a new filtered list
'''
def _removeMults(divider, nums):
  for index, num in enumerate(nums):
    if (num % divider == 0):
      nums[index] = None
  nums = list(filter(None, nums))
  return nums

assert _removeMults(2, list(range(3, 11))) == list(range(3, 11, 2))

'''
  Takes a continous list of integers starting with primes
  Should be merged with removeMults to avoid overhead of moving list around twice
  Should use two pointers to avoid retesting already verified primes
'''
def _findPrimes(nums):
  result = []
  while (len(nums) > 0):
    print(".", end="")
    prime = nums.pop(0)
    nums = _removeMults(prime, nums)
    result.append(prime)
  return result

assert _findPrimes(range(2, 11)) == [2, 3, 5, 7]

'''
  Returns the nth prime
'''
def nthPrime(n):
  primes = _findPrimes([2] + list(range(3, n, 2)))
  while(len(primes) < n):
    primes = _findPrimes(primes + list(range(primes[-1], primes[-1] + n, 2)))
    print(len(primes))
  return primes[n - 1]

assert nthPrime(7) == 15
assert nthPrime(8) == 19
assert nthPrime(9) == 23
assert nthPrime(10) == 29

assert False == True

print(nthPrime(10001))
