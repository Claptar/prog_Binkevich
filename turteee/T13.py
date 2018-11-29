import turtle
a=True
x=0
l=int(input())
b=180 + 180/l
turtle.shape('turtle')

while a:
    for x in range(l):
        turtle.left(b)
        turtle.forward(300)
