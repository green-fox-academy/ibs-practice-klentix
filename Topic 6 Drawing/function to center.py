from tkinter import Tk, Canvas

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
center = 300 / 2

# Create a function that draws a single line and takes 2 parameters:
# The x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# Fill the canvas with lines from the edges, every 20 px, to the center.


def lineToCenter(x, y):
    canvas.create_line(x, y, center, center)


for i in range(0, 301, 20):
    lineToCenter(0, i)
    lineToCenter(i, 0)
    lineToCenter(300, i)
    lineToCenter(i, 300)

root.mainloop()
