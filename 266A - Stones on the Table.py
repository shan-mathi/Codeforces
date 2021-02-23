#108301624	Feb/23/2021 18:45UTC+5.5	Shan_XD	266A - Stones on the Table	PyPy 3	Accepted	186 ms	0 KB

n=int(input())
stones = str(input())
a=stones[0]
count=0
for i in range(1,n):
    if stones[i]==a:
        count+=1
    else:
        a= stones[i]
print(count)
