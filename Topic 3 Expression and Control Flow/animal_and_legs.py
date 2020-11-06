# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

x = int(input("enter value chicken:"))
y = int(input("enter value pig:"))
print('chicken:',x)
print('pig:',y)
legs = x*2+y*4
print("legs:",legs)
