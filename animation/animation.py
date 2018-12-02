from tkinter import *
import graphics as gr


root = Tk()
root.geometry('800x600')
canvas = Canvas(root, bg='white')
Vx_POTATO = 5
X_POTATO = 0
rect_size = 20


def potatoe_move():
    global X_POTATO, rect_size
    canvas.delete(ALL)
    potatoes(X_POTATO, 300, rect_size)
    if X_POTATO < 600:
        X_POTATO += 5
        root.after(100, potatoe_move)


def draw_rect(red, green, blue, x, y, size):
    """
    Рисование отдельного квадратика
    :param red: Красный цвет
    :param green: Зелёный
    :param blue: Синий
    :param x: х Координата квадратика
    :param y: y Коородината квадратика
    :return:
    """
    kvadr = canvas.create_rectangle(x, y, x + size, y + size,
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


def potatoes(x, y, size):
    """
    Рисвание картошечки
    :param x: смещение картошечки по x
    :param y: смещение картошечки по y
    :return:
    """
    color_block(X1, Y1, 249, 201, 41, x, y, size)
    color_block(X2, Y2, 249, 190, 40, x, y, size)
    color_block(X3, Y3, 200, 150, 29, x, y, size)
    color_block(X4, Y4, 148, 103, 21, x, y, size)
    color_block(X5, Y5, 252, 240, 184, x, y, size)
    color_block(X6, Y6, 250, 223, 116, x, y, size)
    color_block(X7, Y7, 250, 223, 110, x, y, size)
    draw_rect(226, 177, 52, x + size * 4, y + size * 4, size)
    draw_rect(211, 163, 42, x + size * 6, y + size * 8, size)
    draw_rect(250, 234, 147, x + size * 2, y + size * 4, size)

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

potatoe_move()
root.mainloop()



