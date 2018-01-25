def factorial(n):
  product = 1
  for i in range (1, n+1):
    product *= i
  return product

def main():
  # example
  print factorial(15)
  print factorial(6)
  print factorial(3)

if __name__== "__main__":
    main()
