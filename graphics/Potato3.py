import graphics as gr
import random

window = gr.GraphWin("Ales' the Binkevich project", 1000, 1000)

'# Рисование отдельного квадратика'


def draw_rect(r, g, b, x, y):
    kvadr = gr.Rectangle(gr.Point(x, y), gr.Point(x + 20, y + 20))
    kvadr.setFill(gr.color_rgb(r, g, b))
    kvadr.setOutline(gr.color_rgb(r, g, b))
    kvadr.draw(window)


def color_block(x, y, r, g, b, a, c):  # Х и Y листы координат для каждого цвета
    i = 0  # i задаёт координаты квадратиков
    for t in range(len(x)):
        draw_rect(r, g, b, a + 20 * x[i], c + 20 * y[i])  # a - смещение картошечки по х
        i += 1  # с - смещение картошечки по y

'#Рисование квадратиков разных цветов'


def potatoes(x, y):
    color_block(X1, Y1, 249, 201, 41, x, y)
    color_block(X2, Y2, 249, 190, 40, x, y)
    color_block(X3, Y3, 200, 150, 29, x, y)
    color_block(X4, Y4, 148, 103, 21, x, y)
    color_block(X5, Y5, 252, 240, 184, x, y)
    color_block(X6, Y6, 250, 223, 116, x, y)
    color_block(X7, Y7, 250, 223, 110, x, y)
    draw_rect(226, 177, 52, x + 20 * 4, y + 20 * 4)
    draw_rect(211, 163, 42, x + 20 * 6, y + 20 * 8)
    draw_rect(250, 234, 147, x + 20 * 2, y + 20 * 4)

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
for i in range (1000):
    potatoes(random.randint(0,1000),random.randint(0,1000))
message = gr.Text(gr.Point(window.getWidth() / 2, 120), 'Potato')
message.setTextColor('yellow')
message.setStyle('italic')
message.setSize(32)
message.draw(window)
window.getMouse()
window.close()
