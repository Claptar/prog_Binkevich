from tkinter import *
import graphics as gr
import random
import time

root = Tk()
root.geometry('800x600')
n = 0
R = 10


def baloon():
    global circle_x, circle_y, R
    circle_x = random.randint(20, 580)
    circle_y = random.randint(20, 580)
    red=random.randint(100, 255)
    green=random.randint(100, 255)
    blue=random.randint(100, 255)
    canv.create_oval(circle_x-R, circle_y-R, circle_x+R, circle_y+R, fill=gr.color_rgb(red, green, blue))


def left_click(event):
    x = event.x
    y = event.y
    global n
    if abs(circle_x - x) < R+1 and abs(circle_y-y) < R+1:
        n += 1




def tick():
    root.after(1000, tick)
    canv.delete(ALL)
    baloon()
    canv.create_text(400, 300, text=n, font='Arial 25')


root.bind('<Button-1>', left_click)

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.mainloop()