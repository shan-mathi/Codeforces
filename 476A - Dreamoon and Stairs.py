#110761411	Mar/22/2021 23:36UTC+5.5	Shan_XD	476A - Dreamoon and Stairs	PyPy 3	Accepted	93 ms	1300 KB

n,m = map(int,input().split())
ans=-1
for p in range(n):
    if (n-p)%m==0 and n>=2*p:
        ans=n-p
print(ans)












