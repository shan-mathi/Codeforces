#111158132	Mar/26/2021 23:24UTC+5.5	Shan_XD	499B - Lecture	PyPy 3	Accepted	234 ms	5700 KB

n,m = map(int,input().split())
traslation = [0]*m
l1=[]
for i in range(m):
    traslation[i]=list(map(str,input().split()))
    l1.append(traslation[i][0])

notes=list(map(str,input().split()))
ans=''


for i in notes:
    id = l1.index(i)
    if len(traslation[id][0])<=len(traslation[id][1]):
        ans+=traslation[id][0]+' '
    else:
        ans += traslation[id][1] + ' '

print(ans.rstrip())


