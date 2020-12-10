# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(source_name,dest_name):
    try:
        with open(source_name) as f:
            with open(dest_name,'w') as f2:
                for line in f:
                    f2.write(line)
                print('copy was successful!')
    except FileNotFoundError:
        print('Please enter correct file name')

copy_file('my-file.txt','my-file2.txt')