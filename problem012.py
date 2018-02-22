'''
  Find smallest triangle number with 500+ dividers
  nth triangle = 1 + 2 ... + n
'''
import math

def _find_triangle(n):
  return int((n + 1) * (n / 2.0))

assert _find_triangle(6) == 21
assert _find_triangle(7) == 28

import math
## from prob 7
def _remove_mults(divider, nums):
  start = nums.index(int(math.pow(divider, 2)))
  for index, num in enumerate(nums[start:]):
    if (num % divider == 0):
      nums[start + index] = None
  nums = list(filter(None, nums))
  return nums
      
'''
  'Sieve of Eratosthenes' from prob 10
'''
def _find_primes(limit):
  result = [2]
  odds = list(range(3, limit, 2))
  while (len(odds) > 0):
    prime = odds.pop(0)
    result.append(prime)
    if (len(odds) > 0 and math.pow(prime, 2) <= odds[-1]):
      odds = _remove_mults(prime, odds)

  return result

primes = primes = _find_primes(50000)

def _find_prime_divisors(n):

  result = []

  for prime in primes:

    if prime > n:
      break

    count = 0
    if n % prime == 0:
      while n % prime == 0:
        n = n // prime
        count += 1
      result.append((prime, count))

  return result

assert _find_prime_divisors(28) == [(2, 2), (7, 1)]

def _count_divisors(n):
  result = 1
  prime_divisors = _find_prime_divisors(n)
  for prime, power in prime_divisors:
    result *= power + 1
  return result

assert _count_divisors(28) == 6

def find_smallest_triangle(bound):
  i = 2
  num_divs = _count_divisors(_find_triangle(i))
  while num_divs < bound:
    i += 1
    num_divs = _count_divisors(_find_triangle(i))
    print(i, num_divs)
  return _find_triangle(i)

assert find_smallest_triangle(5) == 7

print(find_smallest_triangle(500))