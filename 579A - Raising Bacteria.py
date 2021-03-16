#110109410	Mar/16/2021 17:38UTC+5.5	Shan_XD	579A - Raising Bacteria	PyPy 3	Accepted	93 ms	0 KB

n = int(input())
count=0
num=n
while(num>0):
    if num%2==0:
        num=num//2
    else:
        count+=1
        num=num//2
print(count)
