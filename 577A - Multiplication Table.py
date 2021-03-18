#110296409	Mar/18/2021 14:39UTC+5.5	Shan_XD	577A - Multiplication Table	PyPy 3	Accepted	109 ms	1300 KB

n, s = map(int,input().split())
count=0
for i in range(1,n+1):
    if s%i==0 and s//i<=n:
        count+=1

print(count)













