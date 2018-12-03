import turtle
turtle.shape('turtle')
qt = True
k = 20
N = 3
t = 11
while qt:
    for step in range (N):
        turtle.forward(k)
        turtle.left(360/N)
    turtle.penup()
    turtle.right(120)
    turtle.forward(t)
    turtle.left(120)
    turtle.pendown()
    t += 2
    k += 10
    N += 1

