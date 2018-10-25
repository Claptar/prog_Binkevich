from tkinter import *
import graphics as gr
import random


root = Tk()
root.geometry('800x600')


def balloon(x, y):
    r = random.randint(20, 80)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=gr.color_rgb(red, green, blue))


def left_click(event):
    balloon(event.x, event.y)


root.bind('<Button-1>', left_click)

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.mainloop()
