import turtle;
turtle.shape('turtle')
a = True
b = 1
x = int(input())
y = 360/x
turtle.shape('turtle')
while a:
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(y)
