from tkinter import *
import random
import graphics as gr
import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

Balls = []


class Ball:
    def __init__(self, x, y, Vx, Vy, red , green, blue, r):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.design = canvas.create_oval(x, y, x + r, y + r, fill=gr.color_rgb(red, green, blue))
        self.r = r

    def go(self):
        if (self.x + self.r > 600) or (self.x - self.r < 0):
            self.Vx *= -1
        elif (self.y + self.r > 600) or (self.y - self.r < 0):
            self.Vy *= -1
        canvas.move(self.design, self.Vx, self.Vy)
        self.x += self.Vx
        self.y += self.Vy

for i in range(4):
    r = 50
    x = random.randint(100, 600)
    y = random.randint(100, 600)
    Vx = random.randint(-5, 5)
    Vy = random.randint(-5, 5)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    ball_i = Ball(x, y, Vx, Vy, red, green, blue, r)
    Balls.append(ball_i)


"""def babah (vx1, vy1, vx2, vy2, lx, ly):
    nx = -ly
    ny = nx
    vl1 = (vx1 * lx + vy1 * ly) / math.sqrt(lx * lx + ly * ly)
    vl2 = (vx2 * lx + vy2 * ly) / math.sqrt(lx * lx + ly * ly)
    vn1 = (vx1 * nx + vy1 * ny) / math.sqrt(nx * nx + ny * ny)
    vn1 = (vx1 * nx + vy1 * ny) / math.sqrt(nx * nx + ny * ny)
    vl1, vl2 = vl2, vl1
    vx1 = vl1*(lx/math.sqrt(lx*lx + ly*ly)) + vn1*(ny/math.sqrt(nx*nx + ny*ny))
    vx2 = vl1 * (ly / math.sqrt(lx * lx + ly * ly)) + vn1 * (nx / math.sqrt(nx * nx + ny * ny))"""


def tick():
    for k in range(3):
        for m in range(3):
            if k != (m+1):
                if (Balls[k].x - Balls[m+1].x) ** 2 + (Balls[k].y - Balls[m+1].y) ** 2 <= Balls[k].r ** 2:
                    v1 = Vector(Balls[k].Vx, Balls[k].Vy)
                    v2 = Vector(Balls[m+1].Vx, Balls[m+1].Vy)
                    line = Vector(Balls[k].x - Balls[m+1].x, Balls[k].y - Balls[m+1].y)
                    line.x = line.x/math.sqrt(line.x**2 + line.y**2)
                    line.y = line.y/math.sqrt(line.x**2 + line.y**2)
                    normal = Vector(-line.y, line.x)
                    v_line_1 = v1.x * line.x + v1.y * line.y
                    v_line_2 = v2.x * line.x + v2.y * line.y
                    v_normal_1 = v1.x * normal.x + v1.y * normal.y
                    v_normal_2 = v2.x * normal.x + v2.y * normal.y
                    v_line_1, v_line_2 = v_line_2, v_line_1
                    v1.x = v_line_1*line.x + v_normal_1*normal.x
                    v1.y = v_line_1*line.y + v_normal_1*normal.y
                    v2.x = v_line_2 * line.x + v_normal_2*normal.x
                    v2.y = v_line_2 * line.y + v_normal_2*normal.y
                    Balls[k].Vx = v1.x
                    Balls[k].Vy = v1.y
                    Balls[m+1].Vx = v2.x
                    Balls[m+1].Vy = v2.y
    for g in range(4):
        Balls[g-1].go()
    root.after(30, tick)

tick()

canvas.pack(fill=BOTH, expand=1)

root.mainloop()
