from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
size = 10
# Reproduce this:
# [https://github.com/green-fox-academy/teaching-materials/blob/master/workshop/drawing/assets/r4.png]

def drawsquare (x,y,size):
    canvas.create_rectangle(x,y,x+size,y+size, fill='purple')

for i in range(0,7):

root.mainloop()