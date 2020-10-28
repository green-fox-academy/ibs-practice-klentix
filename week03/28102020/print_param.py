# - Create a function called `print_params`
#   which prints the input parameters
#   (can have multiple number of arguments)

param = [(int(input("please input number: ")))]
param2 = [(str(input("please input words: ")))]
def print_params():
    print (param + param2)

print_params()
