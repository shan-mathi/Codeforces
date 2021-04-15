#113058592	Apr/15/2021 10:25UTC+5.5	Shan_XD	1343A - Candies	PyPy 3	Accepted	296 ms	5400 KB

t = int(input())
import math

def candies(n):
    k=1
    x = n/(2**(k+1)-1)
    while(int(x)!=x):
        k+=1
        x = n/((2**(k+1))-1)
    print(int(x))

for i in range(t):
    n= int(input())
    candies(n)
