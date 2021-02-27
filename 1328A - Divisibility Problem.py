#108603046	Feb/27/2021 17:04UTC+5.5	Shan_XD	1328A - Divisibility Problem	PyPy 3	Accepted	280 ms	5300 KB

t = int(input())
for i in range(t):
    a,b = input().split()
    a=int(a)
    b=int(b)
    if a%b==0:
        print(0)
    else:
        print(b-(a%b))
