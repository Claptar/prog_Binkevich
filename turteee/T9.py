import turtle
turtle.shape('turtle')
k=2;
for i in range (6):
    for step in range(90):
        turtle.forward(k);
        turtle.left(4);
    for step in range(90):
        turtle.forward(k);
        turtle.right(4);
    k+=1;
