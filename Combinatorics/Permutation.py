import Factorial

# Finds the number of ways to permute r objects, choosing from n total objects
def permutation(n,r):
    return(Factorial.factorial(n) / (Factorial.factorial(n-r)))
