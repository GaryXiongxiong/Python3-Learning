def phbonaqi():
    n,a,b = 0,0,1
    while True:
        yield(b)
        a,b=b,a+b
        n=n+1
for i in phbonaqi():
    print(i)
    if i > 10000:
        break
