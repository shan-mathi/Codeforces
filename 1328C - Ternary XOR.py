#1328C - Ternary XOR


t= int(input())

def t_xor(n,x):
    a=b='1'
    for i in range(1,n):
        if x[i]=='2':
            if a==b:
                a+='1'
                b+='1'
            elif a>b:
                a+='0'
                b+='2'
            elif b>a:
                b+='0'
                a+='2'
        elif x[i]=='1':
            if a == b:
                a += '1'
                b += '0'
            elif a > b:
                a += '0'
                b += '1'
            elif b > a:
                b += '0'
                a += '1'
        else:
            a+='0'
            b+='0'

    print(a)
    print(b)

for i in range(t):
    n=int(input())
    x=str(input())
    t_xor(n,x)













