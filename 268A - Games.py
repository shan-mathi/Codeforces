#108787688	Mar/01/2021 15:02UTC+5.5	Shan_XD	268A - Games	PyPy 3	Accepted	186 ms	0 KB

n = int(input())
home=[]
guest=[]
for i in range(n):
    h, g = input().split()
    home.append(h)
    guest.append(g)
count=0
for i in home:
    count += guest.count(i)
print(count)
