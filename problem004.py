'''
  Problem: find largest palindromic product of
  two 3 digit numbers (100-999)
'''
import math

def maxPalProduct(digits):
  
  ## define ranges
  minFactor = int(math.pow(10, digits - 1))
  maxFactor = int(math.pow(10, digits) - 1)

  ## initialize loop
  divider = minFactor
  palRoot = maxFactor
  pal = _doubleOrderPal(palRoot)

  while(palRoot >= minFactor):
    while(divider <= (pal / 2) + 1 and divider <= maxFactor):
      dividedPal = pal / divider
      if(pal % divider == 0 and dividedPal > minFactor and dividedPal < maxFactor):
        return pal
      divider += 1
    divider = minFactor

    ## test next largest palindrome
    palRoot -= 1
    pal = _doubleOrderPal(palRoot)

  return null




def _flipNum(num):
  result = 0
  while(num > 0):
    result = (result * 10) + num % 10
    num = int(num / 10)
  return result

assert _flipNum(789) == 987
assert _flipNum(990) == 99
assert _flipNum(401) == 104

def _numOrder(num):
  order = 0
  while(num > 0):
    order += 1
    num = int(num/10)
  return order

assert _numOrder(7) == 1
assert _numOrder(60) == 2
assert _numOrder(909) == 3
assert _numOrder(1674) == 4

def _doubleOrderPal(num):
  return int(num * math.pow(10, _numOrder(num)) + _flipNum(num))

assert _doubleOrderPal(987) == 987789
assert _doubleOrderPal(700) == 700007

assert maxPalProduct(2) == 9009

print(maxPalProduct(3))