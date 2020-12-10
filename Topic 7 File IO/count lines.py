# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

myfile = 'my-file.txt'
try:
    openfile = open(myfile,'r')
    lines = openfile.readlines()
    print(len(lines))
except IOError:
    print ('Zero')
