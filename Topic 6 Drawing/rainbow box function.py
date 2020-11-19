from tkinter import *
import random
from random import randint

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def draw_square (size,colors):
    center = 300/2
    remaining = size/2
    canvas.create_rectangle(center-remaining,center-remaining,center+remaining,center+remaining,fill=colors)

for i in range(len(colors)):
    draw_square(300/2-i*(150/7),colors[i])


# Create a square drawing function that takes 2 parameters:

# The square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# Create a loop that fills the canvas with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).

root.mainloop()



