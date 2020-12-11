#Given a string, compute recursively (no loops)
# a new string where all the lowercase 'x' chars
# have been changed to 'y' chars.

def replacechar(mystr,oldchar,newchar):
    if mystr == '':
        return ''
    elif mystr[0] == oldchar:
        return newchar + replacechar(mystr[1:],oldchar,newchar)
    return mystr[0] + replacechar(mystr[1:],oldchar,newchar)

print(replacechar('this is a sample','x','y'))
print(replacechar('this is a sample','a','o'))
