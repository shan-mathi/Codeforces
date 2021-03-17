#110157609	Mar/17/2021 14:46UTC+5.5	Shan_XD	706B - Interesting drink	PyPy 3	Accepted	1372 ms	10500 KB

import bisect
n=int(input())
x=list(map(int,input().split()))
x.sort()
q=int(input())
for i in range(q):
    m=int(input())
    print(bisect.bisect_right(x,m))
