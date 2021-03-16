#110101271	Mar/16/2021 15:52UTC+5.5	Shan_XD	339B - Xenia and Ringroad	PyPy 3	Accepted	374 ms	10100 KB

n,m = map(int,input().split())
house = list(map(int,input().split()))
time=0
c=1
for i in house:
    if i>c:
        time+=i-c
        c=i
    elif i==c:
        continue
    elif i<c:
        time+=i+(n-c)
        c=i
print(time)


