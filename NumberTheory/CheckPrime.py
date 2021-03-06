# Checks if n is prime, returns boolean
def checkPrime(n):
    if(n == 1):
        return False
    if(n <= 3):
        return True
    if(n%2 == 0 or n%3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i) == 0:
            return False
        i = i + 2
    return True
