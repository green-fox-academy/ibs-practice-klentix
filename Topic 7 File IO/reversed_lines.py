# Create a method that decrypts reversed-lines.txt
def decrypt(file_name):
    with open(file_name, "r") as file:
        foo = file.read().replace('\n', '')
        newline = ''.join(reversed(foo))

    print(newline)

decrypt('reversed-lines.txt')
