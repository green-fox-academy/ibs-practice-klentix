#Given base and n that are both 1 or more,
#compute recursively (no loops) the value of base to the n power,
#so power N(3, 2) is 9 (3 squared).


def recursive_power(base,n):
    if n == 1:
        return base
    if n > 1:
        return base * recursive_power(base,n-1)

base = 6
n = 4
result = recursive_power(base,n)
print (result)