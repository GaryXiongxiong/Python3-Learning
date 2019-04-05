# Use python to draw a python
# turtle库学习
import turtle #海龟库,通过import引入库，调用时使用<库>.<函数>()
#from <库名> import <函数名> 函数名可用*代表所有函数 注意函数重名问题
#turtle.goto(x,y) 绝对坐标

turtle.setup(650,320,200,500) #setup(width,height[,startx][,starty])
turtle.penup()
turtle.fd(-250) #forward by 250 pixel 
#turtle.bk(x) back by x pixel
turtle.pendown()
turtle.pensize(25)#设置画笔宽度 也可用 turtle.width(width)
turtle.pencolor("purple") #颜色名为字符串，rgb默认为小数
#turtle.colormode(mode) mode=1 or 255 改变小数rgb或整数rgb
turtle.seth(-40) #改变行进角度,朝向绝对极坐标系
#turtle.left(angle) 左转相对角度
#turtle.right(angle)右转相对角度
for i in range(4):#range(n)从0到n-1, range(m,n)从m到n-1的数组
    turtle.circle(40,80) #circle(r,angle) 海归左侧找到半径为r的圆心，开始绘制angle度的圆弧
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
