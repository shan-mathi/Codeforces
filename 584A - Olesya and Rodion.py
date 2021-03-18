#110282008	Mar/18/2021 11:28UTC+5.5	Shan_XD	584A - Olesya and Rodion	PyPy 3	Accepted	109 ms	0 KB

n,t = map(int,input().split())
c = int('9'*n)
ans = c- c%t
if ans>0:
    print(ans)
else:
    print(-1)







