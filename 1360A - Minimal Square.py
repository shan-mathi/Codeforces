#109802714	Mar/12/2021 22:36UTC+5.5	Shan_XD	1360A - Minimal Square	PyPy 3	Accepted	264 ms	5300 KB

t= int(input())
for i in range(t):
    x=list(map(int,input().split()))
    x.sort()
    if x[0]*2>x[1]:
        print((x[0]*2)**2)
    else:
        print(x[1]**2)



