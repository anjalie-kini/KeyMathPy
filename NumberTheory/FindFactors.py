from math import sqrt
from functools import reduce

# Finds all factors (prime and composite) of n
def findFactors(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
        ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
