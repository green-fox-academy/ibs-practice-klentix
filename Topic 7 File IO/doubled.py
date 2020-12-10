# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    with open(file_name,"r") as file:
        foo = file.read().replace('\n','')
        newline = ''.join([foo[i] for i in range(len(foo)-1) if foo[i+1]!= foo[i]]+[foo[-1]])
    print (newline)

decrypt('duplicated-chars.txt')