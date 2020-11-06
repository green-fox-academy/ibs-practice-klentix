# Write function that joins the two lists by matching one girl with one boy in a new list
# If someone has no pair, he/she should be the element of the list too
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]

def making_matches(girls,boys):
    matches = []
    for x in range(len(boys)):
        try:
            x == len(girls)
            newgirlslist = girls[x]
        except ValueError:
                print("check again")
        newboyslist = boys[x]
        temp = [newgirlslist,newboyslist]
        matches.append(temp)
    return(matches)



print(making_matches(girls,boys))
