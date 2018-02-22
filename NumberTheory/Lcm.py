import Gcd

def lcm(a, b):
    return (a * b / Gcd.gcd(a, b))
