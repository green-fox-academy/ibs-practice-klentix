# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

x = int(input('how many times program should ask? '))
values = []
for i in range(x):
    values.append(int(input('Please enter a value')))
Sum = sum(values)
Average = sum(values)/len(values)
print ('Sum:',Sum)
print ('Average:',Average)