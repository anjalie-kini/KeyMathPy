import Factorial

# Finds the number of ways to choose r objects from n total objects
def combination(n,r):
    return(Factorial.factorial(n) / (Factorial.factorial(r) * Factorial.factorial(n-r)))
