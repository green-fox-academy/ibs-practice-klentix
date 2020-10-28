#to check if inputs of 2 strings are anagram




def anagram(str1,str2):
    a = list(str1)
    a.sort()
    b = list(str2)
    b.sort()

    return a == b

print(anagram('dog','god'))
