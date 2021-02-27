#108596990	Feb/27/2021 15:25UTC+5.5	Shan_XD	200B - Drinks	PyPy 3	Accepted	216 ms	0 KB

n= int(input())
x = list(map(str, input().split()))
x = [int(i) for i in x]
print( sum(x)/n)
