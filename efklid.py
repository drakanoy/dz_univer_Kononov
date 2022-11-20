import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input())
b = int(input())
print(math.gcd(a, b) == gcd(a, b))
