# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

row = 5
col = row
for i in range (row):
    for j in range (col):
        if i == j:  #to print diag side
            print("*", end= "")
        elif i == 0 or i == (row -1) or j==0 or j == (col-1): #to print outer square
            print ("*", end="")
        else: #print space
            print (" ", end="")

    print()
print ('\nend')