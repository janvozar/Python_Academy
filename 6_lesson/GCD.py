# Task 42: GCD
# GCD - Greatest Common Divisor

def gcd(a,b):
    while b > 1:
        remainder = a % b
        if not remainder:
            break
        a,b = b,remainder
    return b