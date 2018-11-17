from tkinter import *
import random
import graphics as gr

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

r = 20
x = random.randint(100, 300)
y = random.randint(100, 300)
Vx = random.randint(-10, 10)
Vy = random.randint(-10, 10)
red = random.randint(100, 255)
green = random.randint(100, 255)
blue = random.randint(100, 255)

class Ball:
    def __init__(self, x, y, Vx, Vy, red ,green, blue, r):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.design = canvas.create_oval(x, y, x + r, y + r, fill=gr.color_rgb(red, green, blue))

    def go(self, r):
        if (self.x + r > 600) or (self.x - r < 0):
            self.Vx *= -1
        elif (self.y + r > 600) or (self.y - r < 0):
            self.Vy *= -1
        canvas.move(self.design, self.Vx, self.Vy)
        self.x += self.Vx
        self.y += self.Vy

bolik = Ball(x, y, Vx, Vy, red, green, blue, r)


def tick():
    bolik.go(r)
    root.after(10, tick)

tick()

canvas.pack(fill=BOTH, expand=1)

root.mainloop()