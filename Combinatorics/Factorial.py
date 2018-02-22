# Finds n! = 1 x 2 x 3 ... x n
def factorial(n):
  product = 1
  for i in range (1, n+1):
    product *= i
  return product
