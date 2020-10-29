namelist = ['William']
namelist.extend(['Jony', 'Amanda']) # add on multiple items in the list
print("No. of name", len(namelist)) # print total number of items
print("Name list: ", namelist)      # print out each element
print("the 3rd name is:", namelist[2])

#iterate through a list and print out individual name
for i in namelist:
    print(i)

#iterate through a list and print out individual name with index number
for num,name in enumerate (namelist,start = 1):
        print("{}. {}".format(num,name))

#remove 2nd name
namelist.pop(1)
print("after remove 2nd name: ", namelist)

#iterate through a list in reverse order
namelist.reverse()
for k in namelist:
    print("name in reversed order: ", k)

#remove all element
namelist.clear()
print ("namelist after remove all: ", namelist)
print("\nend")

