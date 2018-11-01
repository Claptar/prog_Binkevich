from tkinter import *

root = Tk()
root.geometry("300x300")
canvas = Canvas(root)
x, y = 100, 100
dx, dy = 2, 3
oval = canvas.create_oval(x, y, x+40, y+40)
canvas.pack(fill=BOTH, expand=1)


def tick_handler():
    global x, y, dx, dy
    print("Тик!")
    # Отражение от края холста
    if x < 0:
        dx = -dx
        x = 0
    elif x > 300-40:
        dx = -dx
        x = 300-40
    if y < 0:
        dy = -dy
        y = 0
    elif y > 300-40:
        dy = -dy
        y = 300-40
    x = x + dx; y = y + dy
    canvas.move(oval, dx, dy)


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
speed_scale.set(1);
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()