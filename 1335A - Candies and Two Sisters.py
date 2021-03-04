#109078041	Mar/04/2021 17:55UTC+5.5	Shan_XD	1335A - Candies and Two Sisters	PyPy 3	Accepted	280 ms	5200 KB

n= int(input())

for i in range(n):
    t= int(input())
    if t<=2:
        print(0)
    elif (t%2==0 and t>2):
        print((t-1)//2)
    elif (t%2==1 and t>2):
        print(t//2)
