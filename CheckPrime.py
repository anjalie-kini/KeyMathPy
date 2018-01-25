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

def main():
  # example
  print checkPrime(15)
  print checkPrime(341)
  print checkPrime(3)

if __name__== "__main__":
  main()
