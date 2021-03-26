#111156652	Mar/26/2021 23:02UTC+5.5	Shan_XD	82A - Double Cola	PyPy 3	Accepted	93 ms	0 KB


n= int(input())

r=1
while(5*r<n):
    n-=5*r
    r*=2

ans = (n-1)//r + 1

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
