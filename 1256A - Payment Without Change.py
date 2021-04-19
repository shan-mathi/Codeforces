#113546321	Apr/19/2021 23:18UTC+5.5	Shan_XD	1256A - Payment Without Change	PyPy 3	Accepted	296 ms	6100 KB

def change(a,b,n,S):
    x = S//n
    if x<=a and b>=S%n:
        return 'YES'
    elif x>a and b>=(S- a*n):
        return 'YES'
    else:
        return 'NO'



t = int(input())
for i in range(t):
    a,b,n,S = map(int,input().split())
    print(change(a,b,n,S))
