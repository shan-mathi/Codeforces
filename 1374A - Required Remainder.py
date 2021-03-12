#109801676	Mar/12/2021 22:21UTC+5.5	Shan_XD	1374A - Required Remainder	PyPy 3	Accepted	780 ms	9300 KB


t= int(input())
for i in range(t):
    x,y,n = input().split()
    x=int(x)
    y=int(y)
    n=int(n)
    if n<x:
        print(y)
    elif n%x>y:
        print(n-((n%x)-y))
    elif n%x<y:
        print(n-x-((n%x)-y))
    else:
        print(n)


