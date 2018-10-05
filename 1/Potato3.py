import graphics as gr

window = gr.GraphWin("Ales' the Binkevich project", 1000, 1000)


def draw_rect(r, g, b, x, y):
    kvadr = gr.Rectangle(gr.Point(x, y), gr.Point(x + 20, y + 20))
    kvadr.setFill(gr.color_rgb(r, g, b))
    kvadr.setOutline(gr.color_rgb(r, g, b))
    kvadr.draw(window)


def color_block(X, Y, r, g, b, a, c):
    l = 0
    for t in range(len(X)):
        draw_rect(r, g, b, a + 20 * X[l], c + 20 * Y[l])
        l += 1


def potatoo(a, b):
    color_block(X1, Y1, 249, 201, 41, a, b)
    color_block(X2, Y2, 249, 190, 40, a, b)
    color_block(X3, Y3, 200, 150, 29, a, b)
    color_block(X4, Y4, 148, 103, 21, a, b)
    color_block(X5, Y5, 252, 240, 184, a, b)
    color_block(X6, Y6, 250, 223, 116, a, b)
    color_block(X7, Y7, 250, 223, 110, a, b)
    draw_rect(226, 177, 52, a + 20 * 4, b + 20 * 4)
    draw_rect(211, 163, 42, a + 20 * 6, b + 20 * 8)
    draw_rect(250, 234, 147, a + 20 * 2, b + 20 * 4)


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
potatoo(60, 140)
potatoo(250, 400)
potatoo(600, 200)
message = gr.Text(gr.Point(window.getWidth() / 2, 120), 'Potato')
message.setTextColor('yellow')
message.setStyle('italic')
message.setSize(32)
message.draw(window)
window.getMouse()
window.close()
