#koch.py 绘制科赫曲线
import turtle
def koch(size,n):
    if(n==0):
        turtle.forward(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def initTurtle():
    turtle.setup(1440,900)
    turtle.penup()
    turtle.goto(-700,-100)
    turtle.pensize(1)
    turtle.speed(0)
    turtle.pendown()
initTurtle()
koch(1400,6)
turtle.hideturtle()
turtle.done()