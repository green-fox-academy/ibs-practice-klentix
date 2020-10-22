# Crate a program that draws a chess table like this
#
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
#

row = 8
col = 8
for i in range (row):
    for j in range (col):
        if i==j:
            print ("*", end = " ")
        elif i+j == row-2 or i+j == row-4 or i+j == row-6 or i+j==row or i+j==row+2 or i+j ==row+4:
            print ("*", end = " ")
        else :
            print (" ", end = " ")
    print ()