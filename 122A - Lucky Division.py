#109973487	Mar/14/2021 18:32UTC+5.5	Shan_XD	122A - Lucky Division	PyPy 3	Accepted	218 ms	0 KB

n=int(input())

ans='NO'
for num in range(1,n+1):
    if n%num!=0:
        continue
    count=0
    for i in range(len(str(num))):
        num=str(num)
        if num[i]!='4' and num[i]!='7':
            break
        else:
            count+=1
    if count==len(str(num)):
        ans='YES'

print(ans)
