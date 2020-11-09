from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
colorline1 = canvas.create_line(50,50,50,250,fill="red")
colorline2 = canvas.create_line(50,50,250,50,fill="blue")
colorline3 = canvas.create_line(250,250,250,50,fill='green')
colorline4 = canvas.create_line(250,250,50,250,fill='orange')

# draw a box that has different colored lines on each edge.

root.mainloop()