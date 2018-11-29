import turtle

def curve(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        curve(l/3, n-1)
        turtle.left(60)
        curve(l/3, n-1)
        turtle.right(120)
        curve(l/3, n-1)
        turtle.left(60)
        curve(l/3, n-1)

L = 800
H = L/6*3**0.5
N = 4

turtle.penup()
turtle.goto(-L/2, -H/2)
turtle.pendown()

curve(L, N)