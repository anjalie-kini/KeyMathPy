import Factorial

def permutation(n,r):
    return(Factorial.factorial(n) / (Factorial.factorial(n-r)))
