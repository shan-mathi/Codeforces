#109962852	Mar/14/2021 16:10UTC+5.5	Shan_XD	1A - Theatre Square	PyPy 3	Accepted	93 ms	0 KB

n,m,a = input().split()
import math
n=int(n)
m=int(m)
a=int(a)
print(math.ceil(m/a)*(math.ceil(n/a)))
