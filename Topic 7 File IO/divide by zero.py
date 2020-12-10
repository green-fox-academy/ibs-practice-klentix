# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0


divisor = int(input())
try:
    result = 10 / divisor
    print(result)
except ZeroDivisionError:
    print("fail")