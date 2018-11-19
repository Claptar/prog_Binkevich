from tkinter import *
import random
import graphics as gr

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

Balls = []


class Ball:
    def __init__(self, x_coordinate, y_coordinate, v_x, v_y,
                 red_component, green_component, blue_component, ball_radius):
        self.x = x_coordinate
        self.y = y_coordinate
        self.Vx = v_x
        self.Vy = v_y
        self.design = canvas.create_oval(x, y, x + ball_radius, y + ball_radius,
                                         fill=gr.color_rgb(red_component, green_component, blue_component))
        self.r = ball_radius

    def go(self):
        if (self.x + self.r > 600) or (self.x - self.r < 0):
            self.Vx *= -1
        elif (self.y + self.r > 600) or (self.y - self.r < 0):
            self.Vy *= -1
        canvas.move(self.design, self.Vx, self.Vy)
        self.x += self.Vx
        self.y += self.Vy

for i in range(10):
    radius = random.randint(20, 40)
    x = random.randint(100, 300)
    y = random.randint(100, 300)
    Vx, Vy = 0, 0
    while Vx == 0 and Vy == 0:
        Vx = random.randint(-10, 10)
        Vy = random.randint(-10, 10)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    ball_i = Ball(x, y, Vx, Vy, red, green, blue, radius)
    Balls.append(ball_i)
    """Balls.append(
        Ball(x=random.randint(100, 300),
                  y=random.randint(100, 300), Vx, Vy, red, green, blue, r)
    )"""


def tick():
    for g in range(10):
        Balls[g-1].go()
    root.after(30, tick)

tick()

canvas.pack(fill=BOTH, expand=1)

root.mainloop()
