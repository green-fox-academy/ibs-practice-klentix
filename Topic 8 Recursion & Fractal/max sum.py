#Create a function called maxSum which expects an array of five integers
# as an input parameter and returns the maximum values
# that can be calculated by summing exactly four of the five integers.

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9]))