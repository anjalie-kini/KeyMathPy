def lcm(a, b):
    return a * b / gcd(a, b)

def main():
  # example
  print lcm(15, 12)
  print lcm(24, 36)
  print lcm(2,3)

if __name__== "__main__":
  main()
