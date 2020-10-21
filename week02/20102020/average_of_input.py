# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

x, y, z, a, b = [int(x) for x in input("Enter 5 value: ").split()]
sum = x+y+z+a+b
print ('sum',sum)
average = (x+y+z+a+b)/5
print ('average: {:.2f} '.format(average))


