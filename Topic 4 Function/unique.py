#  Create a function that takes a list of numbers as a parameter
#  Returns a list of numbers where every number in the list occurs only once

#  Example
#print(unique([1, 11, 34, 11, 52, 61, 1, 34]))
#  should print: `[1, 11, 34, 52, 61]`

arr= [1, 11, 34, 11, 52, 61, 1, 34]

def unique(arr):
    return list(dict.fromkeys(arr))

print(unique(arr))