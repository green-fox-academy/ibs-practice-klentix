# Write function that joins the two lists by matching one girl with one boy in a new list
# If someone has no pair, he/she should be the element of the list too
# Expected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]

def making_matches(girls,boys):

    list_both = []
    c = 0
    for n in range(len(boys)):
        list_both.append(boys[n])
        list_both[c + n:c + n] = girls[c + 0:c + 1]
        c += 1
    print(list_both)

making_matches(girls,boys)


