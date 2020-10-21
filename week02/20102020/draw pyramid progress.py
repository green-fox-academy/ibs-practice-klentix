# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

rows = 4
for i in range(1, rows+2):
    print("* " * i)