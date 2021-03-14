#109970851	Mar/14/2021 17:56UTC+5.5	Shan_XD	69A - Young Physicist	PyPy 3	Accepted	186 ms	0 KB

n=int(input())
sumx=sumy=sumz=0
for i in range(n):
    x,y,z=input().split()
    sumx+=int(x)
    sumy+=int(y)
    sumz+=int(z)
if sumx==0 and sumy==0 and sumz==0:
    print('YES')
else:
    print("NO")
