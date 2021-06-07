#118713416	Jun/07/2021 16:21UTC+5.5	Shan_XD	285B - Find Marble	PyPy 3	Accepted	404 ms	10100 KB

def find_marble(n,s,t,x):
    step=0
    while(s!=t and x[s-1]!=0):
        temp = x[s-1]
        x[s-1] = 0
        s = temp
        step+=1
    if s==t:
        return step
    else:
        return -1







n,s,t = map(int,input().split())
x = list(map(int,input().split()))
print(find_marble(n,s,t,x))
