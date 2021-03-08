#109420730	Mar/08/2021 23:52UTC+5.5	Shan_XD	306A - Candies	PyPy 3	Accepted	186 ms	0 KB

n,m = input().split()
n=int(n)
m=int(m)
arr=[n//m]*m
for i in range(n%m):
    arr[-i-1]=arr[-i-1]+1
ans=""
for i in arr:
    ans+=str(i)+" "
print(ans)
