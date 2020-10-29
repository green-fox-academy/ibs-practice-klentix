#Create a map where the keys are strings
# and the values are strings with the following initial values

booklist ={"978-1-60309-452-8":"A Letter to Jo",
           "978-1-60309-459-7":"Lupus",
           "978-1-60309-444-3":"Red Panda and Moon Bear",
           "978-1-60309-461-0":"The Lab"}

# to print out with orders and add on
for x,y in booklist.items():
    print (y + " (ISBN:" + x + ")")

#Remove the key-value pair with key 978-1-60309-444-3
booklist.pop("978-1-60309-444-3")
print("After removing:", booklist)

#Remove the key-value pair with value The Lab
booklist.popitem()
print("Booklist after removing The Lab: ", booklist)

#Add the more key-value pairs to the map
booklist.update({"978-1-60309-450-4":"They Called Us Enemy","978-1-60309-453-5":"Why Did We Trust Him?"})
print("new booklist: ", booklist)


#Print whether there is an associated value with key 478-0-61159-424-8 or not
print("if there is a book 478-0-61159-424-8: ",booklist.get("478-0-61159-424-8"))

#Print the value associated with key 978-1-60309-453-5
for k,v in booklist.items():
    if '978-1-60309-453-5' in k:
        print ("Value matches with 978-1-60309-453-5: ",v)