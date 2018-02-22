# Finds the greatest common divisor between a and b
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
