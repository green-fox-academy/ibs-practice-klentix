# Write a function that checks if the list contains "7"
# if it contains return "Hoorray" otherwise return "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8]
#print(contains_seven(numbers))
# The output should be: "Noooooo"
# Do this again with a different solution using different list functions!

def contains_seven(numbers):
    #print(numbers)
    if "7" in numbers:
        print ("Hoorray")
    else:
        print ("Nooooo")

contains_seven(numbers)