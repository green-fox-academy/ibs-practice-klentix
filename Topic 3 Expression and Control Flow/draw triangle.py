# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was





rows = 4
for i in range(1, rows+1):
    print("* " * i)

#this will print in rows x 6
#for i in range (4):
    #this will print in cols x 5 * * * * *
#    for j in range (i+1):

#        print ("* ", end="")
    #to make sure it falls on new line
#    print()