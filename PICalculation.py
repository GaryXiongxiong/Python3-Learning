#通过随机撒点法求Pi的近似值
from random import random
from time import perf_counter
Darts=5000*5000#抛洒数
hits=0.0#命中圆的数
print("开始运算".center(110,"="))
StartT=perf_counter()
for i in range(1,Darts+1):
    x,y=random(),random()
    dist=(x**2+y**2)**(0.5)
    if dist < 1.0:
        hits=hits+1
    elif dist == 1.0:
        hits=hits+0.5
    print("\r{:5.2f}%  |{:-<100}| {:.2f}s".format((i-1)*100/Darts,"/"*int((i)*100/Darts),perf_counter()-StartT),end="")
    pi=4*(hits/Darts)
print("圆周率为{}".format(pi))
