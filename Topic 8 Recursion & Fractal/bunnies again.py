#We have bunnies standing in a line,
# numbered 1, 2, ...
# The odd bunnies (1, 3, ..) have the normal 2 ears.
# The even bunnies (2, 4, ..) we'll say have 3 ears,
# because they each have a raised foot.
# recursively return the number of "ears" in the bunny line 1, 2, ... n
# (without loops or multiplication).

def recursive_ear(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 2 + recursive_ear(n-1)
    elif n % 2 == 1:
        return 3 + recursive_ear(n-1)

n = 9
total_ears = recursive_ear(n)
print(total_ears)
