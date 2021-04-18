#113407366	Apr/18/2021 16:38UTC+5.5	Shan_XD	1409B - Minimum Product	PyPy 3	Accepted	560 ms	9200 KB

    

def min_product(a,b,x,y,n):
    prod =[]
    # starting from a to x or a-n
    if n> a-x:
        a1=x
        n1=n-(a-x)
        b1 = y if n1>(b-y) else (b-n1)
        prod.append(a1*b1)
    else:
        a1= a-n
        prod.append(a1*b)

    if n> (b-y):
        b2 = y
        n2 = n-(b-y)
        a2 = x if n2 > (a-x) else (a-n2)
        prod.append(a2*b2)
    else:
        b2 = b-n
        prod.append(a*b2)
    print(min(prod))





t = int(input())
for i in range(t):
    a,b,x,y,n = map(int,input().split())
    min_product(a,b,x,y,n)

