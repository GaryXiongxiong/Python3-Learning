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
    turtle.goto(-350,200)
    turtle.pensize(1)
    turtle.speed(0)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
initTurtle()
koch(700,3)
turtle.right(120)
koch(700,3)
turtle.right(120)
koch(700,3)
turtle.hideturtle()
turtle.end_fill()
turtle.done()