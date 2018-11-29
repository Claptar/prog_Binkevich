import turtle
turtle.shape('turtle')
k=0.01;
for i in range (5):
    for step in range(360):
        turtle.forward(k);
        turtle.left(1);
        k=k+0.0003;


