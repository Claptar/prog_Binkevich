import turtle
turtle.shape('turtle')
k = 20
N = 3
t = True
turtle.left(90)
while t:
    for step in range(45):
        turtle.forward(4)
        turtle.right(4)
    for step in range(45):
        turtle.forward(0.5)
        turtle.right(4)
