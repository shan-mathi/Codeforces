#110558936	Mar/20/2021 22:15UTC+5.5	Shan_XD	1352C - K-th Not Divisible by n	PyPy 3	Accepted	155 ms	2900 KB

# to find the nth non divisible number
"""
so... 3rd divisble number will have 3*n-3
you will have to divide the index by 3
take n=4
1,2,3  5,6,7  9,10,11  13,14,15
find 7th
"""

def not_divisible(n,id):
    if id%n==0:
        print((n+1)*((id//n)-1)+n)
    else:
        print((n + 1) * (id // n) + id%n)

t= int(input())
for i in range(t):
    n,id = map(int,input().split())
    not_divisible(n-1,id)

