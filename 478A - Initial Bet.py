#113549351	Apr/19/2021 23:56UTC+5.5	Shan_XD	478A - Initial Bet	PyPy 3	Accepted	93 ms	0 KB

x = list(map(int,input().split()))
if sum(x)%5==0 and sum(x)!=0:
    print(sum(x)//5)
else:
    print(-1)
