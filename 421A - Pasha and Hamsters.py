#109422820	Mar/09/2021 00:30UTC+5.5	Shan_XD	421A - Pasha and Hamsters	PyPy 3	Accepted	93 ms	0 KB

n,a,b=input().split()
arth = list(map(int,input().split()))
alex = list(map(str,input().split()))
ans=['2']*int(n)
for i in arth:
    ans[i-1]='1'
print(" ".join(ans))
