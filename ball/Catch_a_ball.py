from tkinter import *
import graphics as gr
import random
import math


root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
Score = 0
Radius = 20
Miss = 0
Clicks = 0
Score_label = canv.create_text(80, 20, text='Score = {}'.format(Score), font='Arial 25')
Miss_label = canv.create_text(110, 60, text='missclicks = {} '.format(Miss), font='Arial 25')


def balloon():
    global circle_x, circle_y, Radius
    circle_x = random.randint(20, 580)
    circle_y = random.randint(20, 580)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    canv.create_oval(circle_x-Radius, circle_y-Radius, circle_x+Radius, circle_y+Radius,
                     fill=gr.color_rgb(red, green, blue))


def left_click(event):
    """
    :x: x координата клика мышкой
    :y: y координата клика мышкой 
    :return: 
    """
    global Clicks, Score_label, Miss_label
    x = event.x
    y = event.y
    global Score, Miss
    if math.sqrt((circle_x - x)*(circle_x - x)+(circle_y - y)*(circle_y - y)) < Radius+1 and Clicks == 0:
        Score += 1
    elif not math.sqrt((circle_x - x)*(circle_x - x)+(circle_y - y)*(circle_y - y)) < Radius+1:
        Miss += 1
    Clicks += 1
    canv.delete(Score_label, Miss_label)
    Score_label = canv.create_text(80, 20, text='Score = {}'.format(Score), font='Arial 25')
    Miss_label = canv.create_text(110, 60, text='missclicks = {} '.format(Miss), font='Arial 25')


def tick():
    global Clicks, Score_label, Miss_label
    Clicks = 0
    root.after(1000, tick)
    canv.delete(ALL)
    balloon()
    Score_label = canv.create_text(80, 20, text='Score = {}'.format(Score), font='Arial 25')
    Miss_label = canv.create_text(110, 60, text='missclicks = {}'.format(Miss), font='Arial 25')

root.bind('<Button-1>', left_click)


canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.mainloop()
