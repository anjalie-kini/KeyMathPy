import Gcd

# Finds the least common multiple of a and b
def lcm(a, b):
    return (a * b / Gcd.gcd(a, b))
