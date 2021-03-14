#109962852	Mar/14/2021 16:10UTC+5.5	Shan_XD	1A - Theatre Square	PyPy 3	Accepted	93 ms	0 KB

n,m,a = input().split()
n=int(n)
m=int(m)
a=int(a)
if m%a==0 and n%a==0:
    print((m//a)*(n//a))
elif (m%a!=0 and n%a!=0):
    print((m//a + 1)*(n//a + 1))
elif (m%a!=0) and n%a==0:
    print((m//a + 1)*(n//a))

elif (m%a==0) and n%a!=0:
    print((m // a) * (n // a + 1))

