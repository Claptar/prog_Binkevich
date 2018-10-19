from tkinter import *
import time



def tick():
    root.after(200, tick)
    canv.delete(ALL)
    canv.create_text(400, 300, text=time.strftime('%H:%M:%S'), font='Arial 25')


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)
root.mainloop()