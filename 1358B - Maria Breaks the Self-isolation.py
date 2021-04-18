#113409623	Apr/18/2021 17:07UTC+5.5	Shan_XD	1358B - Maria Breaks the Self-isolation	PyPy 3	Time limit exceeded on test 4	2000 ms	12400 KB

def n_grannies(n, x):
    x.sort(reverse = True)
    while (len(x)<max(x)):
        p = max(x)
        x = [i for i in x if i!=p]
        if len(x)==0:
            break
 
    print(len(x)+1)
 
 
 
 
 
 
t = int(input())
for i in range(t):
    n= int(input())
    x = list(map(int,input().split()))
    n_grannies(n,x
