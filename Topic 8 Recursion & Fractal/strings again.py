#Given a string,
# compute recursively a new string where
# all the 'x' chars have been removed.

def remove(char, mystr):
    if not mystr:
        return ''
    if char == mystr[0]:
        return remove(char, mystr[1:])
    else:
        return mystr[0] + remove(char, mystr[1:])

print(remove('i','this is a sample'))