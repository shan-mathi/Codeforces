#109761527	Mar/12/2021 13:15UTC+5.5	Shan_XD	172A - Phone Code	PyPy 3	Accepted	684 ms	5800 KB

n= int(input())

str1= str(input())
ctr = len(str1)
for i in range(2,n+1):
    strn = str(input())
    ans=0
    for j in range(ctr):
        if str1[j]!=strn[j]:
            break
        else:
            ans+=1
    ctr=ans


print(ctr)
