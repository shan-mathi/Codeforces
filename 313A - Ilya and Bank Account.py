#113059051	Apr/15/2021 10:35UTC+5.5	Shan_XD	313A - Ilya and Bank Account	PyPy 3	Accepted	216 ms	0 KB

n = int(input())
if n>=0:
    print(n)
else:
    num= str(n)
    if int(num[1:-1])>int(num[1:-2]+num[-1]):
        print(-1*int(num[1:-2]+num[-1]))
    else:
        print(-1*int(num[1:-1]))
