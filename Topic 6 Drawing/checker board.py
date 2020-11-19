from tkinter import *

root = Tk()

size = 30
color = 'white'
canvas = Canvas(root, width='300', height='300')
canvas.pack()

for i in range(10):  #row
    for h in range(10): #col
        x1 = i * size
        y1 = h * size
        x2 = x1+size
        y2 = y1+size
        canvas.create_rectangle(x1,y1,x2,y2,fill = color)
        if color == 'white':
            color = 'black'
        else:
            color = 'white'

    if color == 'white':
        color = 'black'
    else:
        color ='white'
# Fill the canvas with a checkerboard pattern.

root.mainloop()