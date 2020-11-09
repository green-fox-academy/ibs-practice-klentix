from tkinter import *

root = Tk() #create a blank window

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackline = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

#canvas.delete(redLine) #remove certain thing
#canvas.delete(ALL) # remove all in the canvas
root.mainloop()  #make sure the window displays continuosly until you close it=> it breaks the loop
