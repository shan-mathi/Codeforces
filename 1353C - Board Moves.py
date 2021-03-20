#110553291	Mar/20/2021 20:54UTC+5.5	Shan_XD	1353C - Board Moves	PyPy 3	Accepted	108 ms	0 KB

t = int(input())

def middle(n):
    o = (n-1)//2
    print(8*o*(o+1)*(2*o+1)//6)


for i in range(t):
    n= int(input())
    middle(n)


















