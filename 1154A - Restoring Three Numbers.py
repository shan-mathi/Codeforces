#109173846	Mar/05/2021 23:40UTC+5.5	Shan_XD	1154A - Restoring Three Numbers	PyPy 3	Accepted	77 ms	0 KB

x=list(map(int,input().split()))
ans=list(map(lambda i:str(max(x)-i),x))
ans.remove('0')
print(" ".join(ans))

