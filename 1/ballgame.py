from tkinter import *

root = Tk()
root.geometry("300x300")
canvas = Canvas(root)
x, y = 100, 100
r = 40
oval = canvas.create_oval(x, y, x+r, y+r)
canvas.pack(fill=BOTH, expand=1)
balls: list
ball: list

for i in range(5):
    m = canvas.create_oval(x, y, x+r, y+r)
    Vx = i
    Vy = 2*i
    ball.append(m)
    ball.append(Vx)
    ball.append(Vy)
    balls.append(ball)


def tick_handler():
    for i in range (5)
        canvas.move(balls[i][j], , dy)


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
