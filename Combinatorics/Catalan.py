import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

# Finds the nth Catalan number
def catalan(n):
    return (1 / n * ncr(2*n, n-1))
