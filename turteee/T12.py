import turtle
turtle.shape('turtle')
k = 20
N = 3
turtle.pen(fillcolor='yellow')
turtle.begin_fill()
for step in range(90):
    turtle.forward(7)
    turtle.left(4)
turtle.end_fill()
turtle.pen(fillcolor='blue')
turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(40)
turtle.pendown()
turtle.begin_fill()
for step in range(90):
    turtle.forward(1)
    turtle.left(4)
turtle.end_fill()
turtle.penup()
turtle.left(180)
turtle.forward(80)
turtle.pendown()
turtle.begin_fill()
for step in range(90):
    turtle.forward(1)
    turtle.right(4)
turtle.end_fill()
turtle.penup()
turtle.left(180)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.pendown()
turtle.pen(fillcolor='blue',pencolor='black',pensize=4)
turtle.forward(40)
turtle.penup()
turtle.forward(40)
turtle.pen(fillcolor='blue',pencolor='red',pensize=4)
turtle.left(90)
for step in range(22):
    turtle.forward(2)
    turtle.left(4)
turtle.right(180)
turtle.pendown()
for step in range(45):
    turtle.forward(2)
    turtle.right(4)




