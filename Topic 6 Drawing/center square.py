from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(size):
    center = 300/2
    remaining =  size/2
    mysquare = canvas.create_rectangle(center-remaining,center-remaining,center+remaining,center+remaining,fill='green')

print(draw_square(10))

#greenbox = canvas.create_rectangle(145,145,155,155, fill='green')

# draw a green 10x10 square to the center of the canvas.

root.mainloop()
