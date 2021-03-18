#110292902	Mar/18/2021 13:51UTC+5.5	Shan_XD	1342A - Road To Zero	PyPy 3	Accepted	93 ms	0 KB

def road2zero(x,y,a,b):
    if x*y>=0:
        if b>2*a:
            count=(a*abs(x+y))
        else:
            count= (b-a)*(min(abs(x),abs(y)))+ a*max(abs(x),abs(y))
    else:
        count= (abs(x)+ abs(y))*a
    return count

t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    a,b= map(int,input().split())
    print(road2zero(x,y,a,b))












