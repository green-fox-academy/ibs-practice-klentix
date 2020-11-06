# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stored number is lower
# You found the number: 8

x = int(input('Enter number:'))
for i in range (0,10):
    if x==i < 8:
        print ('the stored number is higher')
    elif x==i > 8:
        print ('the stored number is lower')
    elif x== i == 8:
        print ('you found the number:8')

