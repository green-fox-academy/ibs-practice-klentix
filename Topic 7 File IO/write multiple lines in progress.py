# Create a function that takes 3 parameters: a path, a word and a number
# and is able to write into a file.
# The path parameter should be a string that describes the location of the file you wish to modify
# The word parameter should also be a string that will be written to the file as individual lines
# The number parameter should describe how many lines the file should have.
# If the word is "apple" and the number is 5, it should write 5 lines
# into the file and each line should read "apple"
# The function should not raise any errors if it could not write the file.

def write_line(file_name,new_word,lines_of_new_word):
    #open file in append and read mode
    with open(file_name,"a+") as file:
        #move read cursor to the start of the file
        file.seek(0)
        data = file.read()
        #if file is not empty, then append:
        for i in range(lines_of_new_word):
            if len(data) > 0:
                file.write("\n")
        #append text at the end of the file:
            file.write(new_word + "\n")
    print ("Added!")
write_line('new-file.txt','apple',5)


