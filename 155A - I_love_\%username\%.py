#109168751	Mar/05/2021 22:16UTC+5.5	Shan_XD	155A - I_love_\%username\%	PyPy 3	Accepted	248 ms	1400 KB

n= int(input())
t = list(map(int, input().split()))
count=0
for i in range(1,n):
    if t[i]>max(t[:i]) or t[i]<min(t[:i]):
        count+=1
print(count)
