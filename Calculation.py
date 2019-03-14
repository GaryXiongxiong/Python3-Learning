#Python数学运算特点
x=3+3.0 #复合数据类型混合运算，结果为更宽松的数据类型
print(x)
x=3+3j
print(x)
print(3/4) #int÷int结果为float
print(3//4) #//为整除
print(abs(-3))#绝对值函数
print(divmod(5,3))#商余函数
print(pow(2,3))#pow(x,y[,z])=x ^ y mod z
print(round(3.1415925,3))#round(x,y)保留x的y位小数四舍五入
print(max(1,6,4,9,3))
print(min(2,1,6,4,2))#返回最大值与最小值
print(int(13.5))
print(float(13))
print(complex(13))