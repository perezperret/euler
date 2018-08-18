mem = {}

def collatz_length(n, count=0):
  try:
    return count + mem[n]
  except:
    pass
  if(n == 1): return count + 1
  if(n % 2 == 0):
    return collatz_length(n // 2, count + 1)
  else:
    return collatz_length(3*n + 1, count + 1)

assert collatz_length(13) == 10

def longest_collatz(limit):
  result = 0
  value = 0
  for i in range(1, limit):
    val = collatz_length(i)
    mem[i] = val
    if(val > value):
      result = i
      value = val
  return result

# print(longest_collatz(int(1e6)))
# print(collatz_length(837799))
# >>> 837799
