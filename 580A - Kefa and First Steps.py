#113057012	Apr/15/2021 09:51UTC+5.5	Shan_XD	580A - Kefa and First Steps	PyPy 3	Accepted	171 ms	10700 KB

n = int(input())
x = list(map(int,input().split()))
lenx=1
p=1
for i in range(1,n):
    if x[i]>=x[i-1]:
        p+=1
        lenx = max(lenx,p)
    else:
        p=1
print(lenx)
