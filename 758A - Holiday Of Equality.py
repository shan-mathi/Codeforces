#109173492	Mar/05/2021 23:34UTC+5.5	Shan_XD	758A - Holiday Of Equality	PyPy 3	Accepted	93 ms	1200 KB

n=int(input())
x=list(map(int,input().split()))
print(sum(map(lambda i:max(x)-i,x)))



