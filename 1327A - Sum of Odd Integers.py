#111153101	Mar/26/2021 22:10UTC+5.5	Shan_XD	1327A - Sum of Odd Integers	PyPy 3	Accepted	1341 ms	9300 KB

def check_odd(n,k):
    if n>=k**2 and (n+k)%2==0:
        return 'YES'
    else:
        return 'NO'

t=int(input())
for i in range(t):
    n,k = map(int,input().split())
    print(check_odd(n,k))
