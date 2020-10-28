# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

rows = 4
listofnumbers = [[0] * rows for i in range(rows)]
for i in range(rows):
    for j in range(rows):
        if i < j:
            listofnumbers[i][j] = 0
        elif i > j:
            listofnumbers[i][j] = 0
        else:
            listofnumbers[i][j] = 1
for row in listofnumbers:
    print(' '.join([str(elem) for elem in row]))