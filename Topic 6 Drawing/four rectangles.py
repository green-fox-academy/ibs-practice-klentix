from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
def random_color():
    return random.randint(0,0x1000000)
for x in range (0,4):
    color = '{:06x}'.format(random_color())
    x1 = random.randint(10,300)
    y1 = random.randint(10,300)
    x2 = random.randint(10,300)
    y2 = random.randint(10,300)
    my_rectangle = canvas.create_rectangle(x1,y1,x2,y2,fill=('#'+color))

# Draw four different size and color rectangles.
# Avoid code duplication.

root.mainloop()
