#calculating mersenne primes
import math

def prime(b):
    for possibleprime in range(2,b):
        isprime = True
        for num in range(2, possibleprime):
            if possibleprime % num == 0:
                isprime = False
        if isprime:
            primes.append(possibleprime)
    return primes

def Mersenne(b):
    for d in range(b):
        f=((2**(d))-1) 
        if f%2 != 0:
            e.append(f)
    return e

def intersection(primes, e):
    M = [value for value in primes if value in e]
    return M

primes = []
e = []
b=200000      
prime(b)
Mersenne(b)
M=intersection(primes,e)
print(M)