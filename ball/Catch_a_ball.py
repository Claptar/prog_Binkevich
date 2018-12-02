from tkinter import *
import graphics as gr
import random
import math


root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
SCORE = 0
RADIUS = 20
MISS = 0
CLICKS = 0
Score_label = canv.create_text(80, 20, text='Счёт = {}'.format(SCORE), font='Arial 25')
Miss_label = canv.create_text(110, 60, text=' Промахи = {} '.format(MISS), font='Arial 25')


def balloon():
    global circle_x, circle_y, RADIUS
    circle_x = random.randint(20, 580)
    circle_y = random.randint(20, 580)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    canv.create_oval(circle_x-RADIUS, circle_y-RADIUS, circle_x+RADIUS, circle_y+RADIUS,
                     fill=gr.color_rgb(red, green, blue))


def left_click(event):
    """
    :x: x координата клика мышкой
    :y: y координата клика мышкой 
    :return: 
    """
    global CLICKS, Score_label, Miss_label
    x = event.x
    y = event.y
    global SCORE, MISS
    if math.sqrt((circle_x - x)**2+(circle_y - y)**2) <= RADIUS and CLICKS == 0:
        SCORE += 1
    elif not math.sqrt((circle_x - x)**2+(circle_y - y)**2) <= RADIUS:
        MISS += 1
    CLICKS += 1
    canv.delete(Score_label, Miss_label)
    Score_label = canv.create_text(80, 20, text='Счёт = {}'.format(SCORE), font='Arial 25')
    Miss_label = canv.create_text(110, 60, text=' Промахи = {} '.format(MISS), font='Arial 25')


def tick():
    global CLICKS, Score_label, Miss_label, MISS
    if CLICKS == 0:
        MISS += 1
    CLICKS = 0
    root.after(1000, tick)
    canv.delete(ALL)
    balloon()
    Score_label = canv.create_text(80, 20, text='Счёт = {}'.format(SCORE), font='Arial 25')
    Miss_label = canv.create_text(110, 60, text=' Промахи = {}'.format(MISS), font='Arial 25')

root.bind('<Button-1>',  left_click)


canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.mainloop()
