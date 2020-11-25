
# https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/train/python
# https://www.codewars.com/kata/573182c405d14db0da00064e/train/python

# A natural number is called k-prime if it has exactly k prime factors, counted with multiplicity.
# A natural number is thus prime if and only if it is 1-prime.

# 9 = 3 * 3 --so 2
# 12 = 3 * 2 * 2 --so 3


# def is_K_primt(k,intIn):

import math

k = 3
intIn = 12
primeFactor = 0

# get list of primes
def getPrimes(intIn):
    maxVal = int(intIn/2) # limit test upper range
    prime = []
    for x in range(2,maxVal):
        count = 0
        for y in range(2,x):
            if x % y == 0:
                count += 1
        if count == 0:
            prime.append(x)
    return prime

def getFactors(intIn):
    maxVal = int(intIn/2) # limit test upper range
    factor = []
    for x in range(1,maxVal+1):
        if intIn % x == 0:
            factor.append(x)
    return factor

# divide int by all less than value
print(getPrimes(intIn))
print(getFactors(intIn))

factors = getFactors(intIn)
primes = getPrimes(intIn)

for i,x in enumerate(factors):
    for y in primes:
        if x % y == 0 and x / y > 1:
            factors[i] = int(x / y)
            factors.append(int(x - (x / y)))

outList = [x for x in factors if x in primes]

print(factors)
print(factors[::-1])
print(outList)
# print('The prime factor of {} is {}'.format(intIn,primeFactor))