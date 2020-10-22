#for j in range (4):
#    for i in range (4):
#        print ("*  ",end ="")
#    print()


row = int(input("please enter"))
col = int(input("please enter"))
for i in range(row):
    for j in range(col):
        if i == 0 or i==row-1 or j == 0 or j==col-1:
            print("*", end ="")
        else:
            print(" ", end="")
    print()