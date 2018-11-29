import turtle
turtle.shape('turtle')
k=10;
for i in range (10):
    for step in range (4):
        turtle.forward(k);
        turtle.left(90);
    turtle.penup();
    turtle.backward(5);
    turtle.right(90);
    turtle.forward(5);
    turtle.left(90);
    turtle.forward(0);
    turtle.pendown();
    k+=10;

