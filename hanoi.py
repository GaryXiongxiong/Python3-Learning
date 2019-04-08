#hanio.py Learning about recursive functions
count = 0
def hanio(n,src,mid,dst):
    global count
    if n == 1:
        print("{: <3d}:{}->{}".format(1,src,dst))
        count = count+1
    else:
        hanio(n-1,src,dst,mid)
        print("{: <3d}:{}->{}".format(n,src,dst))
        count = count+1
        hanio(n-1,mid,src,dst)
x = eval(input("汉诺塔层数："))
hanio(x,"A","B","C")
print("共移动{}次".format(count))
