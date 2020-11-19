import os
import sys

def print_usage():
    print("Command Line Todo Application\n"
           "=============================\n"
           'Command line arguments:\n\t'
           '-l  lists all undone tasks\n\t'
           '-la lists all the tasks\n\t'
           '-a  adds a new task\n\t'
           '-r  removes a task\n\t'
           '-c  completes a task\n\t')

def list_tasks():
    #open the task file for reading
    f = open('tasks.txt',"r")
    filesize = os.path.getsize("tasks.txt")
    lines = f.readlines()
    count = 0
    if filesize == 0:
        print("No to-do for today!")  #handle the file missing exception
    else:
        content_list = f.readlines() #read all task in the list
        for line in lines: #numbering task
            count += 1
            if "." not in line:
                print("{}-[ ] {}".format(count, line.strip()))  #showing only undone task
    #close the file when done
    f.close()

def list_all_tasks():
    f = open('tasks.txt', "r")
    filesize = os.path.getsize("tasks.txt")
    lines = f.readlines()
    count = 0
    if filesize == 0:
        print("No to-do for today!")  # handle the file missing exception
    else:
        content_list = f.readlines()  # read all task in the list
        for line in lines:  # numbering task
            count += 1
            if "." not in line:
                print("{}-[ ] {}".format(count, line.strip()))  # showing only undone task
            else:
                print("{}-[x] {}".format(count, line.strip().replace(".","")))
    # close the file when done
    f.close()

def add_task():
    argument = sys.argv
    # open the task file for append
    with open('tasks.txt','a') as f:
        if len(argument) < 3 and argument[1]=='-a':
            # handle the file missing exception
            print("Unable to add: no task provided")
        else:
            # append the new task to the end of the file
            f.write("\n"+ argument[2])
        # close the file when done
        f.close()

 #f.write("\n"+ input("enter a task: "))


def remove_task():
        try:
            # open the task file for reading
            with open('tasks.txt', 'r') as f:
                #to convert sysargv argument to interger so can use it later
                argument = (int(sys.argv[2])-1)
                #convert txt file data to list
                lines = f.readlines()
                f. close()
                #print(argument)
                #print(lines)
                #indexing argument and put in in a list of data to remove
                lines[argument] = ""
            # open the task file for editing
            with open('tasks.txt','w') as f:
                new_file ="".join(lines)
                f.write(new_file)
                f.close()
                readable_file = open('tasks.txt')
                read_file=readable_file.read()
                print('task is removed')
                exit()
        # handle the file missing exception
        except IndexError:
            print("Unable to remove: index is out of bound")
        except IndentationError:
            print("Unable to remove: no task provided")
        except ValueError:
            print("Unable to remove: index is not a number")


def complete_task():
    try:
        # open the task file for reading
        with open('tasks.txt', 'r') as f:
            # to convert sysargv argument to integer so can use it later
            argument = (int(sys.argv[2])-1)
            # convert txt file data to list
            lines = f.readlines()
            temp = lines[argument]
            #to mark x! in a line where argument is
            lines[argument] = (temp+".")
            #write to temp new file
            my_file = open('tasks.txt','w')
            new_file_contents ="".join(lines)
            my_file.write(new_file_contents)
            my_file.close()
            readable_file = open("tasks.txt")
            read_file =readable_file.read()
            readable_file.close()
            print("Task is completed: " + temp)
 #       with open('tasks.txt','r') as f3:
 #           count = 0

 #           for line in f3.readlines():
 #               count += 1
 #               if "x!" in str(f3.readlines()):
 #                   print("{}-[x] {}".format(count, line.strip()))
 #               else:
 #                   print("{}-[ ] {}".format(count, line.strip()))



    # handle the file missing exception
    except IndexError:
        print("Unable to check: index is out of bound")
    except IndentationError:
        print("Unable to check: no task provided")
    except ValueError:
        print("Unable to check: index is not a number")

print (sys.argv)  #show the absolute path of the application



if len(sys.argv) == 1:
    print_usage()
elif sys.argv[1] == '-l':
    list_tasks()
elif sys.argv[1] == '-la':
    list_all_tasks()
elif sys.argv[1] == '-a':
    add_task()
elif sys.argv[1] == '-r':
    remove_task()
elif sys.argv[1] == '-c':
    complete_task()
else:
    print("Unsupported argument")
    print_usage()