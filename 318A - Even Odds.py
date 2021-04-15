#113057287	Apr/15/2021 09:58UTC+5.5	Shan_XD	318A - Even Odds	PyPy 3	Accepted	218 ms	0 KB

n,k = map(int,input().split())
if n%2==0:
    odd = n//2
else:
    odd = (n+1)//2

if k>odd:
    print((k-odd)*2)
else:
    print(2*k-1)
