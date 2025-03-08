#1
def Huiwen1(x):
    x = str(x)
    n = len(x)
    l = int(n / 2)
    y = ''
    for i in range(l):
        if x[i] != x[n - i - 1]:
            print("Huiwen1:",False)
            y = 'False'
            break
    if y != 'False':
        print("Huiwen1:",True)
#2
def Huiwen2(x):
    if x < 0:
        print("Huiwen2:",False)
    else:
        x = str(x)
        l = len(x)
        y = [None for _ in range(l)]
        for i in range(l):
            y[l - 1 - i] = x[i]
        x = list(x)
        if x == y:
            print("Huiwen2:",True)
        else:
            print("Huiwen2:",False)
x= int(input("请输入一个数："))
Huiwen1(x)
Huiwen2(x)