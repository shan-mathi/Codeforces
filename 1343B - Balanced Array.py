#109171857	Mar/05/2021 23:06UTC+5.5	Shan_XD	1343B - Balanced Array	PyPy 3	Accepted	217 ms	14700 KB

t=int(input())
for i in range(t):
    n=int(input())
    if n%4!=0:
        print('NO')
    else:
        ans=[str(i) for i in range(2,n+1,2)]
        ans2=[str(i) for i in range(1,n-2,2)]
        ans2.append(str(n+int(n/2)-1))
        print('YES')
        print(" ".join(ans+ans2))

