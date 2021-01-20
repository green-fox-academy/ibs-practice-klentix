#  Create a function that takes a string and a list of string as a parameter
#  Returns the index of the string in the list where the first string is part of
#  Only need to find the first occurence and return the index of that
#  Returns `-1` if the string is not part any of the strings in the list

#  Example
#print(substrlist("ching", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `4`
#print(substrlist("not", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `-1`

def substrlist(strg,word):
    for item in word:
        match = item.find(strg)
        if match != -1:
            break
    print (match)

(substrlist("ching",["this", "is", "what", "I'm", "searching", "in"]))
(substrlist("not", ["this", "is", "what", "I'm", "searching", "in"]))

