import turtle
scr = turtle.Screen()
scr.title("Triangle")
scr.bgcolor("black")
scr.setup(800,800)
pen = turtle.Turtle()
pen.color("red")
pen.pensize(5)
pen.shape("turtle")
pen.fillcolor()
pen.begin_fill()
pen.penup()
pen.goto(-200,-50)
pen.pendown()
for i in range(3):
    pen.fd(400)
    pen.lt(120)
pen.end_fill()
pen.hideturtle()

