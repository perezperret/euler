'''
  Problem: sum of multiples of 3 and 5 under 1000
'''
def sumOfMultiplesOf3and5(number):
    nums = range(0, number)
    result = 0

    for num in nums:
        if((num % 3 == 0) or (num % 5 == 0)):
            result += num

    return(result)

assert sumOfMultiplesOf3and5(10) == 23
print(sumOfMultiplesOf3and5(1000))