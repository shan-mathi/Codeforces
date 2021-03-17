#110147904	Mar/17/2021 12:18UTC+5.5	Shan_XD	489B - BerSU Ball	PyPy 3	Accepted	93 ms	0 KB

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
b.sort()
if n>m:
    temp=a.copy()
    a=b.copy()
    b=temp.copy()
ap=bp=0
pair=0
while(ap<len(a) and bp<len(b)):
    if abs(a[ap]-b[bp])<=1:
        pair+=1
        ap+=1
        bp+=1
    elif a[ap]>b[bp]+1:
        bp+=1
    else:
        ap+=1
print(pair)
