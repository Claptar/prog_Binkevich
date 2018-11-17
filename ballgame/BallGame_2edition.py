from tkinter import *
import random
import graphics as gr

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

for i in range(10):
    r = random.randint(20, 40)
    x =
    y = random.randint(100, 300)
    Vx = random.randint(-10, 10)
    Vy = random.randint(-10, 10)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    Balls.append(
        Ball(x=random.randint(100, 300),
                  y=random.randint(100, 300), Vx, Vy, red, green, blue, r)
    )



def foo():
    print(x)

def tick():
    for g in range(10):
        Balls[g-1].go()
    root.after(30, tick)

tick()

canvas.pack(fill=BOTH, expand=1)

root.mainloop()
