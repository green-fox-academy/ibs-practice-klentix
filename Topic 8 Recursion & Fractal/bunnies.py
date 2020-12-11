#We have a number of bunnies and
# each bunny has two big floppy ears.
# We want to compute the total number of ears
# across all the bunnies recursively (without loops or multiplication).


def recursive_ear(bunnies):
    ear = 2
    if bunnies == 0:
        return 0
    return ear + recursive_ear(bunnies-1)

bunnies = 4
total_ears = recursive_ear(bunnies)
print (total_ears)