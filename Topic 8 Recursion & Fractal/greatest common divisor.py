#Find the greatest common divisor of two numbers using recursion.

def recursive_gcd(a,b):
    #if b = 0 then return a as biggest common divisor
    if b == 0:
        return a
    else:
        return recursive_gcd(b,a%b)

print(recursive_gcd(192,270))