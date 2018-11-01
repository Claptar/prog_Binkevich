from tkinter import *
import random

root = Tk()
root.geometry("800x800")
canvas = Canvas(root)
r = 40
canvas.pack(fill=BOTH, expand=1)
balls = []
ball = []

for i in range(5):
    x = random.randint(100, 600)
    y = random.randint(100, 600)
    Vx = random.randint(1, 5)*i
    Vy = random.randint(1, 5)*i
    ball.append(canvas.create_oval(x, y, x+r, y+r))
    ball.append(Vx)
    ball.append(Vy)
    balls.append(ball)


def tick_handler():
    global balls, ball, x, y
    for j in range(5):
        canvas.move(balls[j-1][0], balls[j-1][1], balls[j-1][2])


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)

def unfreezer(event):
    global freeze
    if freeze == True:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)

speed_scale = Scale(root, orient=HORIZONTAL, length=300,
               from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

# Скорость = 1
speed_scale.set(1)
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()
