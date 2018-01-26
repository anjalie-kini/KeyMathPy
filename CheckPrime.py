def checkPrime(n):
    if(n == 1):
        return false
    if(n == 2):
        return true
    for i in range(2,n):
        if (num % i) == 0:
            return false
        else:
            return true
