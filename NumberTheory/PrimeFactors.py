# Finds all prime factors of n
def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n /= i
            factors.append(i)
    if n > 1:
        factors.append(int(n))
    return factors
