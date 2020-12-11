#Given a string, compute recursively a new string where all the adjacent chars are now separated by a *

def recur_add_star(mystr):
    if len(mystr)==1:
        return mystr
    elif len(mystr)>1:
        return mystr[0] + "*" + recur_add_star(mystr[1:])

print (recur_add_star('sample'))