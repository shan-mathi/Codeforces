#119191468	Jun/12/2021 00:17UTC+5.5	Shan_XD	486B - OR in Matrix	PyPy 3	Accepted	124 ms	2300 KB

def b_to_a(b,a,m,n):
    for i in range(m):
        for j in range(n):
            if b[i][j]==0:
                a[i] = [0]*n
                for k in range(m):
                    a[k][j]=0
    return a


def a_to_c(a,c,m,n):
    for i in range(m):
        for j in range(n):
            if a[i][j]==1:
                c[i] = [1]*n
                for k in range(m):
                    c[k][j] =1
    return c

def b_and_c(b,c):
    return b==c

if __name__ == '__main__':
    m,n = map(int,input().split())
    b=[]
    a=[[1]*n]*m
    c =[[0]*n]*m
    for i in range(m):
        b.append(list(map(int,input().split())))
    a = b_to_a(b,a,m,n)
    c = a_to_c(a,c,m,n)
    if b_and_c(b,c):
        print('YES')
        for i in range(m):
            print(" ".join(map(lambda x: str(x),a[i])))
    else:
        print('NO')





