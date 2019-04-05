#文本进度条
import time
import math
print("程序开始".center(20,"="))
time_start=time.perf_counter()
for i in range(101):
    fi=i+math.sin(i*math.pi*20)/80
    print("\r{:5.2f}%".format(fi)+"[{:-<100}]".format("/"*int(fi))+"  {:.2f}s".format(time.perf_counter()-time_start),end="")#通过格式化字符串一行代码搞定
    #print("\r{:5}%".format(i)+"[{:-<100}]".format("/"*int(i))+"  {:.2f}s".format(time.perf_counter()-time_start),end="")
    time.sleep(0.1)
print("\n"+"程序结束".center(20,"="))