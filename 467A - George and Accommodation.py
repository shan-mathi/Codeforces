#108532778	Feb/26/2021 16:46UTC+5.5	Shan_XD	467A - George and Accommodation	PyPy 3	Accepted	93 ms	0 KB

n=int(input())
count=0
for i in range(n):
    p,q = input().split()
    if int(q)-int(p)>1:
        count+=1
print(count)
