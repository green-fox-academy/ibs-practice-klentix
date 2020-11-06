# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements in `numbers`

numbers = [3, 4, 5, 6, 7]
#total 25
total = 0                        #so that it add on
for i in range(0,len(numbers)):  #i represent index
    total = total+numbers[i]     #taking index number and add to total

print("sum of the elements: ",total)