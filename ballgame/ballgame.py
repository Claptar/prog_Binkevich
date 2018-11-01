from tkinter import *
import random

root = Tk()
root.geometry("800x800")
canvas = Canvas(root)
r = 40
canvas.pack(fill=BOTH, expand=1)
ball = []

for i in range(5):
    x = random.randint(100, 600)
    y = random.randint(100, 600)
    Vx = random.randint(1, 3)*i
    Vy = random.randint(1, 3)*i
    ball.append(canvas.create_oval(x, y, x+r, y+r, fill = "red"))
    ball.append(Vx)
    ball.append(Vy)


def tick_handler():
    global ball
    for j in range(5):
        canvas.move(ball[3*j], ball[3*j+1], ball[3*j+2])


def time_handler():
    speed = speed_scale.get()
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300,
               from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

# Скорость = 1
speed_scale.set(1)
freeze = False

root.after(10, time_handler)
root.mainloop()
