import Factorial

def combination(n,r):
    return(Factorial.factorial(n) / (Factorial.factorial(r) * Factorial.factorial(n-r)))
