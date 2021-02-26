#108534359	Feb/26/2021 17:14UTC+5.5	Shan_XD	344A - Magnets	PyPy 3	Accepted	1496 ms	4400 KB

n=int(input())
mem= str(input())
group=1
for i in range(1,n):
    inp= str(input())
    if mem!= inp:
        group+=1
        mem=inp
print(group)
