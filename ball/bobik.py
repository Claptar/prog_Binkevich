from tkinter import *
import graphics as gr
import random
import math
import time

root = Tk()
root.geometry('800x600')
score = 0
R = 20
miss = 0
clicks = 0


def baloon():
    global circle_x, circle_y, R
    circle_x = random.randint(20, 580)
    circle_y = random.randint(20, 580)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    canv.create_oval(circle_x-R, circle_y-R, circle_x+R, circle_y+R, fill=gr.color_rgb(red, green, blue))


def left_click(event):
    global clicks
    x = event.x
    y = event.y
    global score, miss
    if math.sqrt((circle_x - x)*(circle_x - x)+(circle_y - y)*(circle_y - y)) < R+1 and clicks == 0:
        score += 1
    elif not math.sqrt((circle_x - x)*(circle_x - x)+(circle_y - y)*(circle_y - y)) < R+1:
        miss += 1
    clicks += 1


def tick():
    global clicks
    clicks = 0
    root.after(3000, tick)
    canv.delete(ALL)
    baloon()
    canv.create_text(80, 20, text="score", font='Arial 25')
    canv.create_text(140, 20, text=score, font='Arial 25')
    canv.create_text(80, 60, text="missclicks", font='Arial 25')
    canv.create_text(180, 60, text=miss, font='Arial 25')


root.bind('<Button-1>', left_click)

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.mainloop()
