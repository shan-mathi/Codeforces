#111158644	Mar/26/2021 23:30UTC+5.5	Shan_XD	43A - Football	PyPy 3	Accepted	216 ms	0 KB

n = int(input())
A= str(input())
count=1
for i in range(1,n):
    team = str(input())
    if team==A:
        count+=1
    else:
        B=team
if count>n-count:
    print(A)
else:
    print(B)




