from turtle import *
t=Turtle() # creating object of turtle class
t.speed(1) #help('turtle.speed')
t.shape('turtle')
t.pensize(10)
# t.pencolor('green')
# t.fillcolor('green')
t.color('green','#d4670a')
t.begin_fill()
t.forward(100)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(100)
for i in range(3):
    t.left(90)
    t.fd(100)
t.end_fill()
t.penup()
t.forward(100)
t.pendown()
t.fd(100)
for i in range(3):
    t.left(90)
    t.fd(100)
done()