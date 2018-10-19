import graphics as gr

window = gr.GraphWin("Ales' the Binkevich project", 1000, 1000)

# Рисование квадратиков
def draw_rect(r, g, b, x, y):
    kvadr = gr.Rectangle(gr.Point(x, y), gr.Point(x + 20, y + 20))
    kvadr.setFill(gr.color_rgb(r, g, b))
    kvadr.setOutline(gr.color_rgb(r, g, b))
    kvadr.draw(window)

"""Набор кооржинат для рисования квадратиков разных цветов"""
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

#Рисование квадратиков квадратиков разных цветов по столбцам

colomn = 0;
for t in range(len(X1)):
    draw_rect(249, 201, 41, 200 + 20 * X1[colomn], 200 + 20 * Y1[colomn])
    colomn += 1;
colomn = 0;
for t in range(len(X2)):
    draw_rect(249, 190, 40, 200 + 20 * X2[colomn], 200 + 20 * Y2[colomn])
    colomn += 1;
colomn = 0;
for t in range(len(X3)):
    draw_rect(200, 150, 29, 200 + 20 * X3[colomn], 200 + 20 * Y3[colomn])
    colomn += 1;
colomn = 0;
for t in range(len(X4)):
    draw_rect(148, 103, 21, 200 + 20 * X4[colomn], 200 + 20 * Y4[colomn])
    colomn += 1;
colomn = 0;
for t in range(len(X5)):
    draw_rect(252, 240, 184, 200 + 20 * X5[colomn], 200 + 20 * Y5[colomn])
    colomn += 1;
colomn = 0;
for t in range(len(X6)):
    draw_rect(250, 223, 116, 200 + 20 * X6[colomn], 200 + 20 * Y6[colomn])
    colomn += 1;
colomn = 0;
for t in range(len(X7)):
    draw_rect(250, 223, 110, 200 + 20 * X7[colomn], 200 + 20 * Y7[colomn])
    colomn += 1;

#Рисование одиночных квадратиков, на которые не понадобился набор координат

draw_rect(226, 177, 52, 200 + 20 * 4, 200 + 20 * 4)
draw_rect(211, 163, 42, 200 + 20 * 6, 200 + 20 * 8)
draw_rect(250, 234, 147, 200 + 20 * 2, 200 + 20 * 4)


message = gr.Text(gr.Point(window.getWidth() / 2, 120), 'Potato')
message.setTextColor('yellow')
message.setStyle('italic')
message.setSize(32)
message.draw(window)
window.getMouse()
window.close()
