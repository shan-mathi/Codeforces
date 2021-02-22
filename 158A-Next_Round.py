#108172331	Feb/22/2021 17:01UTC+5.5	Shan_XD	158A - Next Round	PyPy 3	Accepted	216 ms	0 KB

n,k= input().split()
x = list(map(str, input().split()))
count=0
for i in range(int(n)):
    if int(x[i])>=int(x[int(k)-1]) and int(x[i])>0:
        count+=1
print(count)
