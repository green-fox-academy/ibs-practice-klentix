from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
size = 10
# Reproduce this:
# [https://github.com/green-fox-academy/teaching-materials/blob/master/workshop/drawing/assets/r3.png]

for i in range(1,20):
    x1 = i*size
    y1 = i*size
    x2 = x1+size
    y2 = y1+size
    canvas.create_rectangle(x1,y1,x2,y2, fill = 'purple')

root.mainloop()