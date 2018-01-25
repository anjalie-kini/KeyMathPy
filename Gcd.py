def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def main():
  # example
  print gcd(15, 12)
  print gcd(24, 36)
  print gcd(2,3)

if __name__== "__main__":
  main()
