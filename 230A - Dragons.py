#110099733	Mar/16/2021 15:32UTC+5.5	Shan_XD	230A - Dragons	PyPy 3	Accepted	248 ms	2000 KB

s,n = map(int,input().split())
opp=[0]*n
for i in range(n):
    opp[i]=(list(map(int,input().split())))
opp= sorted(opp,key=lambda x: x[0])

for opp in opp:
    if s>opp[0]:
        s+=opp[1]
    else:
        s=-1
        break
if s>0:
    print('YES')
else:
    print('NO')

