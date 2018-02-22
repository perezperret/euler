'''
  Problem: find smallest number divisible by [1 - 20]
'''

def compactFactorial(num):
  dividers = list(range(1, num + 1))
  factors = []
  result = 1
  for divider in dividers:
    if(result % divider != 0):
      for factor in factors:
        if(divider % factor == 0):
          result /= factor
          factors.remove(factor)
      result *= divider
      factors.append(divider)
  return int(result)

assert compactFactorial(10) == 2520
assert compactFactorial(20) == 232792560

print(compactFactorial(20))