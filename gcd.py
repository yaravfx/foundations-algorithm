# Find the greatest common denominator of two numbers
# Using Euclid's algorithm

def gcd(a, b):
    while b != 0:
        # temp = a
        # a = b
        # b = temp % a
        a, b = b, a % b
    return a

print(gcd(20, 8))
print(gcd(60, 96))
