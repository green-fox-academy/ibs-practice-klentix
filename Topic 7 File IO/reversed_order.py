# Create a method that decrypts reversed-order.txt

def decrypt(file_name):
    with open(file_name, "r") as file:
        foo = file.readlines()
        for line in reversed(foo):
            print(line)

decrypt('reversed-order.txt')