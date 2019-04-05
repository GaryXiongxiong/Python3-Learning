#conditional output
n = eval(input())
if n == 0 :
    print("Hello World")
elif n > 0:
    for i in range(0,11,2):
        print("Hello World"[i:i+2:1])
else:
    for i in range(11):
        print("Hello World"[i])