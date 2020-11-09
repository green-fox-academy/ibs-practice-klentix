from tkinter import *
from random import randint
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.

def tothecenter(x,y):
    canvas.create_line(x, y, 150, 150)

for i in range(3):
    tothecenter(randint(0, 300),randint(0, 300))
# Draw at least 3 lines with that function using a loop.


canvas.mainloop()