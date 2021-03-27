#111234353	Mar/28/2021 00:01UTC+5.5	Shan_XD	1363A - Odd Selection	PyPy 3	Accepted	156 ms	

t= int(input())

def odd_sum(n,l):
    eve=0
    odd=0
    t=0
    for i in l:
        if i%2==0:
            eve+=1
        else:
            odd+=1

    m = min(eve,n-1)
    fill = n-m
    if fill%2==0:
        fill+=1
    if odd>=fill and fill<=n:
        return 'Yes'
    else:
        return 'No'


for i in range(t):
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    print(odd_sum(x,l))






