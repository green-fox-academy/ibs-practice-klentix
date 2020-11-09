from tkinter import *
from random import randint
import random


root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws one square and takes 1 parameters:
# The square size
def random_color():
    return random.randint(0,0x1000000)

def draw_square(size):
    color = '{:06x}'.format(random_color())
    center = 300/2
    remaining = size/2
    canvas.create_rectangle(center - remaining, center-remaining, center + remaining, center + remaining,fill = '#'+color)

# and draws a square of that size to the center of the canvas.
for i in range(0,4):
    draw_square(randint(50,100))
# Draw 3 squares with that function.
# Avoid code duplication.

root.mainloop()