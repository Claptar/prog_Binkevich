from tkinter import *
import graphics as gr
import random

root = Tk()
root.geometry('800x600')
canvas = Canvas(root, bg='white')
Vx_POTATO = 5
X_POTATO = 0
rect_size = 20
LIST = []


class Potatoe:

    def __init__(self, x, y, size, vx, vy):
        self.x = x
        self.y = y
        self.size = size
        self.vx = vx
        self.vy = vy

    def view(self):
        """
            Рисование картошечки
            """
        color_block(X1, Y1, 249, 201, 41, self.x, self.y, self.size)
        color_block(X2, Y2, 249, 190, 40, self.x, self.y, self.size)
        color_block(X3, Y3, 200, 150, 29, self.x, self.y, self.size)
        color_block(X4, Y4, 148, 103, 21, self.x, self.y, self.size)
        color_block(X5, Y5, 252, 240, 184, self.x, self.y, self.size)
        color_block(X6, Y6, 250, 223, 116, self.x, self.y, self.size)
        color_block(X7, Y7, 250, 223, 110, self.x, self.y, self.size)
        draw_rect(226, 177, 52, self.x + self.size * 4, self.y + self.size * 4, self.size)
        draw_rect(211, 163, 42, self.x + self.size * 6, self.y + self.size * 8, self.size)
        draw_rect(250, 234, 147, self.x + self.size * 2, self.y + self.size * 4, self.size)

    def go(self):
        self.view()
        if (self.x > 510) or (self.x < 0):
            self.vx *= -1
        elif (self.y > 510) or (self.y < 0):
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy


def big_potato():
    """
    двигает большую картошину
    :return:
    """
    global POTATO, LIST
    canvas.delete(ALL)
    POTATO.go()
    canvas.create_rectangle(2, 2, 550, 550)
    if POTATO.x < 300:
        root.after(30, big_potato)
    else:
        canvas.delete(ALL)
        for i in range(20):
            LIST.append(Potatoe(510, random.randint(200, 400), 3, random.randint(-5, -3), random.randint(-5, 5)))
        potatoe_crash()


def potatoe_crash():
    """
    создаёт и двигает маленькие картошинки
    :return:
    """
    global LIST
    canvas.delete(ALL)
    canvas.create_rectangle(2, 2, 550, 550)
    for i in range(20):
        LIST[i-1].go()
    root.after(10, potatoe_crash)


def draw_rect(red, green, blue, x, y, size):
    """
    Рисование отдельного квадратика
    :param red: Красный цвет
    :param green: Зелёный
    :param blue: Синий
    :param x: х Координата квадратика
    :param y: y Коородината квадратика
    :param size: размер картошечки
    :return:
    """
    canvas.create_rectangle(x, y, x + size, y + size,
                            outline=gr.color_rgb(red, green, blue),
                            fill=gr.color_rgb(red, green, blue))


def color_block(x, y, red, green, blue, a, c, size):
    """
    Рисование квадратиков одного цвета
    :param x: x координата картошечки
    :param y: y координата картошечки
    :param red: красая компонента квадратика
    :param green: зелёная компонента квадратика
    :param blue: синяя компонента квадратика
    :param a: смещение картошечки по х
    :param c: смещение картошечки по y
    :param size: размер одного квадратика
    :return:
    """
    g = 0
    for t in range(len(x)):
        draw_rect(red, green, blue, a + size * x[g], c + size * y[g], size)  # a - смещение картошечки по х
        g += 1  # с - смещение картошечки по y


"""Набор координат для квадратиков каждого цвета (Данным образом бысрее записывать координаты)"""
X1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 8, 8]
Y1 = [4, 5, 6, 7, 3, 7, 8, 2, 6, 7, 8, 7, 8, 1, 7, 8, 1, 1, 4, 5, 4, 5, 6]
X2 = [2, 4, 4, 5, 7, 7, 8, 9, 10, 10, 10]
Y2 = [2, 1, 9, 9, 3, 8, 7, 6, 3, 4, 5]
X3 = [1, 2, 3, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 11, 11]
Y3 = [8, 9, 9, 3, 9, 2, 6, 9, 1, 8, 2, 7, 2, 6, 7, 3, 4, 5, 6]
X4 = [4, 5, 6, 6, 7, 7, 8, 9, 10, 11, 12, 12, 12]
Y4 = [10, 10, 7, 10, 7, 10, 9, 8, 8, 7, 4, 5, 6]
X5 = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6]
Y5 = [3, 4, 5, 3, 5, 6, 3, 4, 5, 4]
X6 = [2, 2, 4, 5, 6, 8, 8]
Y6 = [5, 6, 2, 2, 2, 2, 3]
X7 = [5, 6, 6, 9, 9, 9]
Y7 = [6, 5, 6, 3, 4, 5]


canvas.pack(fill=BOTH, expand=1)
POTATO = Potatoe(0, 200, 20, 5, 0)
big_potato()
root.mainloop()
