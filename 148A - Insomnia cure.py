#108598440	Feb/27/2021 15:49UTC+5.5	Shan_XD	148A - Insomnia cure	PyPy 3	Accepted	248 ms	1500 KB

k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
count=0
for i in range(1,d+1):
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        count+=1
print(count)
