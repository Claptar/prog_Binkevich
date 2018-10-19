from tkinter import *
import graphics as gr
import random
import time


def bobik():
    x = random.randint(20, 580)
    y = random.randint(20, 580)
    canv.create_oval(x-10, y-10,x+10, y+10,fill=gr.color_rgb(random.randint(100, 255), random.randint(100, 255), random.randint(100 , 255)))


def tick():
    root.after(1000, tick)
    canv.delete(ALL)
    bobik()

root.bind('<Button-1>',left_button)

def left_button(event):
    root.title("Left")
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.mainloop()