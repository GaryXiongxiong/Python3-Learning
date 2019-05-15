# 凑硬币问题，现有x,y,z面值的硬币若干，求凑出n元需要的最少硬币数
# 面对xyz，有f(a)=b，即凑a元需要b个硬币
# 且f(a)=min(f(a-x),f(a-y),f(a-z))+1 [a-x,a-y,a-z>0]因为在f(a-x)的基础上加上x面值硬币一枚可得f(a)，yz同理，选择最少的情况
# 可得动态规划生成方法
def coin(x,y,z,n):
    coins = [x,y,z]
    f = [0]
    change = [0]
    for i in range(1,n+1):
        arr = [i-value for value in coins if i-value >= 0]
        f.append(1+f[min(arr)])
    return f[n]
if __name__ == "__main__":
    str = input()
    arr = [eval(i) for i in str.split(" ")]
    assert len(arr) == 4,'参数数量错误'
    print(coin(arr[0],arr[1],arr[2],arr[3]))
