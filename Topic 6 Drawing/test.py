from tkinter import Tk, Canvas

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a square drawing function that takes 2 parameters:
# The square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# Create a loop that fills the canvas with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def drawSquareColored(size, color):
    x = 300 / 2
    y = 300 / 2
    scenter = size / 2
    canvas.create_rectangle(x - scenter, y - scenter, x + scenter, y + scenter, fill=color)


for i in range(len(colors)):
    drawSquareColored(300 - i * 42, colors[i])
    print(300 - (300 / (len(colors) - i)))

root.mainloop()
