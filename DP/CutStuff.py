# 切钢条问题，长度为0-10的刚条单独卖的价格为：p = [0,1,5,8,9,10,17,17,20,24,30]，问长度为n的刚条，最好的切割方法是什么
# 类似于凑硬币问题，f(a)=b，a长度的钢条最大价值为b
# f(a) = max(f(a-m)+p(m))[for m in range(11)][a-m>0] 即a长度的钢条价值为 a-m长度最大价值 + m长度的价值
# 可得动态规划方程
def cut(p,n):
    f = [0]
    for a in range(1,n+1):
        value = []
        for m in range(1,len(p)):
            if a-m>=0:
                value.append(f[a-m]+p[m])
            else:
                continue
        f.append(max(value))
    return f
if __name__ == "__main__":
    print(cut([0,1,5,8,9,10,17,17,20,24,30],20))
