#109082824	Mar/04/2021 18:59UTC+5.5	Shan_XD	510A - Fox And Snake	PyPy 3	Accepted	108 ms	0 KB

n,m= input().split()
n=int(n)
m=int(m)
for i in range(1,n+1):
    if i%2==1:
        print('#'*m)
    elif i%4==0:
        print('#'+'.'*(m-1))
    else:
        print('.'*(m-1)+'#')
