# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

def pyramid(rows):
   #rows = 5
    for i in range (rows):
        print (" "*(rows-i-1)+"*"*(rows+2*i-(rows-1))) #print upper pyramid
    for j in range (rows-1,0,-1):
        print (" "*(rows-j)+"*"*(j*2-1)) #print lower pyramid
    print()
pyramid(5) #change row here