#111161169	Mar/27/2021 00:09UTC+5.5	Shan_XD	467B - Fedor and New Game	PyPy 3	Accepted	140 ms	1900 KB

n,m,k = map(int,input().split())
army=[]
for i in range(m):
    x = int(input())
    army.append(x)
m= int(input())
ans=0


for i in army:
    uniq = bin(m^i)
    count=0
    for j in uniq:
        if j=='1':
            count+=1
            if count<=k:
                continue
            else:
                count=k+1
                break
    if count<=k:
        ans+=1
print(ans)







