#110517838	Mar/20/2021 13:58UTC+5.5	Shan_XD	474B - Worms	PyPy 3	Accepted	358 ms	13100 KB

import bisect
n=int(input())
x=list(map(int,input().split()))
a=[x[0]] + [0]*(n-1)
for i in range(1,n):
    a[i]=a[i-1]+x[i]

m=int(input())
q=list(map(int,input().split()))
for i in q:
    print(bisect.bisect_left(a,i)+1)
















