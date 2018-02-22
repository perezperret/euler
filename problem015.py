## lattice paths from 0,0 to n,n = combinations of n*2 in n (searched)
## solution from euler docs

cache = {}

def count_paths(m, n):

  if m == 0 or n == 0:
    return 1

  try:
    return cache[(m, n)]
  except KeyError:
    cache[(m, n)] = count_paths(m, n - 1) + count_paths(m - 1, n)
    return cache[(m, n)]

print(count_paths(20, 20))