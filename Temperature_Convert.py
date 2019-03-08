#Temperature_convert.py

Tempstr = input("请输入温度")
if Tempstr[-1] in [ 'F' , 'f' ]:
	C = (eval(Tempstr[0:-1]) - 32)/1.8 #通过字符串切片[0:-1]剔除最后一个字符
	print("输出温度为：{:.2f}C".format(C))
elif Tempstr[-1] in ['C' , 'c' ]:
	F = eval(Tempstr[0:-1])*1.8+32
	print("输出温度为：{:.2f}F".format(F))
else:
	print("输入格式有误，请查证")
