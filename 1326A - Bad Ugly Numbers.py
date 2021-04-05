#112064479	Apr/05/2021 15:31UTC+5.5	Shan_XD	1326A - Bad Ugly Numbers	PyPy 3	Accepted	998 ms	7600 KB

def ugly_nos(n):
    s= int('9'*n)
    ctrl=1
    while(ctrl and s>int('9'*(n-1))):
        for i in str(s):
            if i=='0':
                s-=1
                break
            elif s%int(i)==0:
                s-=1
                break
        ctrl=0
        print(s)

t = int(input())
for i in range(t):
    n= int(input())
    if n==1:
        print(-1)
    else:
        ugly_nos(n)


