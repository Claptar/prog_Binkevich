from tkinter import *
import random
import graphics as gr

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
r = 40
canvas.pack(fill=BOTH, expand=1)
ball = []

for i in range(20):
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    x = random.randint(100, 600)
    y = random.randint(100, 600)
    vx = random.randint(-2, 2)*i
    vy = random.randint(-2, 2)*i
    ball.append(canvas.create_oval(x, y, x+r, y+r, fill=gr.color_rgb(red, green, blue)))
    ball.append(vx)
    ball.append(vy)
    ball.append(x)
    ball.append(y)


def tick_handler():
    global ball, r
    for j in range(20):
        x_velocity = ball[5 * j+1]
        y_velocity = ball[5 * j+2]
        x_ball= ball[5 * j+3]
        x_ball = ball[5 * j + 4]
        if x_ball < 0:
            x_velocity *= -1
            x_ball = 0
        elif x_ball > 600 - r:
            x_velocity *= -1
            x_ball = 600 - r
        if x_ball < 0:
            y_velocity *= -1
            x_ball = 0
        elif x_ball > 600 - r:
            y_velocity *= -1
            x_ball = 600 - r
        x_ball += x_velocity
        x_ball += y_velocity
        canvas.move(ball[5*j], x_velocity, y_velocity)
        ball[5*j + 1] = x_velocity
        ball[5*j + 2] = y_velocity
        ball[5*j + 3] = x_ball
        ball[5*j + 4] = x_ball


def time_handler():
    speed = speed_scale.get()
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

root.after(10, time_handler)
root.mainloop()