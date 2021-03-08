#109415137	Mar/08/2021 22:18UTC+5.5	Shan_XD	432A - Choosing Teams	PyPy 3	Accepted	93 ms	1600 KB

n,k = input().split()
x = list(map(int,input().split()))

count=0
for i in x:
    if i<=(5-int(k)):
        count+=1
print(count//3)


