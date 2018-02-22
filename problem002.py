'''
  Problem: Sum of even fibonacci numbers under 4e6.
  Some efficiency can be gained by running the sum in a 
  single function, however the solution was accaptable
  for the requirement
'''

def fib(limit):
  ## no fibs smaller than 0
  if(limit == 0):
    return([0])
  ## at least fib of 1
  result = [0, 1, 1];
  ## create fib list
  while(result[-1] <= limit):
    val = result[-1] + result[-2]
    result.append(result[-1] + result[-2])
  ## verify last inserted is within limit
  if(result[-1] > limit):
    del result[-1]
  ## return list
  return result

assert fib(25) == [0, 1, 1, 2, 3, 5, 8, 13, 21]

def sumEvens(nums):
  result = 0
  for num in nums:
    if(num % 2 == 0):
      result += num
  return result

assert sumEvens(fib(25)) == 10
print(sumEvens(fib(4e6)))