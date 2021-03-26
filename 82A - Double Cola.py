#111156025	Mar/26/2021 22:54UTC+5.5	Shan_XD	82A - Double Cola	PyPy 3	Accepted	124 ms	0 KB

import math
n= int(input())

ctl=0
while(5*(2**(ctl) -1) < n):
    ctl+=1
if n<6:
    cycle = n
else:
    cycle = n - 5*(2**(ctl-1)-1)
ans = math.ceil(cycle/2**(ctl-1))

if ans==1:
    print('Sheldon')
elif ans==2:
    print('Leonard')
elif ans==3:
    print('Penny')
elif ans==4:
    print('Rajesh')
elif ans==5:
    print('Howard')
else:
    print('weird')
