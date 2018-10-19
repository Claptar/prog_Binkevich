from tkinter import *
import graphics as gr
import random
import time


def bobik():
    r1 = random.randint(20, 580)
    r2 = random.randint(20, 580)
    canv.create_oval(r1-10, r2-10, r1+10, r2+10,fill=gr.color_rgb(random.randint(100, 255), random.randint(100, 255), random.randint(100 , 255)))


def tick():
    root.after(1000, tick)
    canv.delete(ALL)
    bobik()


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.mainloop()