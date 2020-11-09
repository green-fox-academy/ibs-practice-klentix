from tkinter import Tk, Canvas

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# Draw at least 3 lines with that function using a loop.


def drawHorizontalLine(x, y):
    canvas.create_line(x, y, x+300, y)


for i in range(0, 300, 5):
    drawHorizontalLine(15, i)

root.mainloop()