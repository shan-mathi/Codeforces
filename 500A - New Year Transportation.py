#110105013	Mar/16/2021 16:47UTC+5.5	Shan_XD	500A - New Year Transportation	PyPy 3	Accepted	109 ms	3700 KB

n,t = map(int,input().split())
x= list( map(int,input().split()))
i=0
while(i<n):
    if t==i+1:
        print('YES')
        break
    elif t<i+1:
        print('NO')
        break
    else:
        i+=x[i]
        continue


