#109419906	Mar/08/2021 23:36UTC+5.5	Shan_XD	386A - Second-Price Auction	PyPy 3	Accepted	93 ms	0 KB

n=int(input())
x=list(map(int,input().split()))
c=x.copy()
c.sort()
print(x.index(max(x))+1, c[-2] )


