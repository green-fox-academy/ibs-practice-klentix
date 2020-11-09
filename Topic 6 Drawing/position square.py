from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws one square and takes 2 parameters:

def draw_square(x,y):
    x==y
    canvas.create_rectangle(x,y,x+10,y+10,fill='yellow')
# The x and y coordinates of the square's top left corner
print (draw_square(50,50))
# and draws a 50x50 square from that point.
for i in range (0,3):
    draw_square(randint(0,300),randint(0,300))
# Draw 3 squares with that function.
# Avoid code duplication.

root.mainloop()