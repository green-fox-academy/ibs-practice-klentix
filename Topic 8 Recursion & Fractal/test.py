def removechar(mystr,char):
    if char == mystr[0]:
        return removechar(mystr[1:],char)
    else:
        return mystr[0] + removechar(mystr[1:], char)

print (removechar('this is a sample','t'))

