#113433662	Apr/18/2021 23:02UTC+5.5	Shan_XD	1333A - Little Artem	PyPy 3	Accepted	77 ms	

def sgrid(m,n):
    if m==1:
        print('B\nW'+'B\n'*(m-2))
    else:
        print('WB'+'B'*(n-2)+'\n'+(('B'*n+'\n')*(m-2))+ 'B'*n)

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    sgrid(n,m)
