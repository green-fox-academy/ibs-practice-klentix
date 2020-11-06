# Write a function called `sum` that returns the sum of numbers from zero to the given parameter

#num = int(input( "enter a integer: " ))
num = 6
total = 0
def sum(num):
    for i in range (0,num):
        num += i
    print(num)
sum(num)

#0,1,2,3,4
#0,1,2,3,4,5,6
