#108531341	Feb/26/2021 16:21UTC+5.5	Shan_XD	110A - Nearly Lucky Number	PyPy 3	Accepted	216 ms	0 KB

n=str(input())

lucky=0
for i in n:
    if i=='4' or i=='7':
        lucky+=1
ans='YES'
for i in str(lucky):
    if i!='4' and i!='7':
        ans='NO'
        break
print(ans)
