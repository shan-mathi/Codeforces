#109083315	Mar/04/2021 19:05UTC+5.5	Shan_XD	581A - Vasya the Hipster	PyPy 3	Accepted	124 ms	0 KB

a,b= input().split()
a=int(a)
b=int(b)
print("{} {}".format(min(a,b),(max(a,b)-min(a,b))//2))
