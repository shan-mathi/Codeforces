#110098187	Mar/16/2021 15:10UTC+5.5	Shan_XD	492B - Vanya and Lanterns	PyPy 3	Accepted	109 ms	0 KB

n,l = map(int,input().split())
x=list(map(int,input().split()))
x.sort()
d = x[0]
for i in range(1, n):
    d = max(x[i] - x[i - 1], d)

if x[0]==0 and x[-1]==l:
    print(float(d / 2))

else:
    print(max(float(d/2),x[0],l-x[-1]))
