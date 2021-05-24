#117267080	May/25/2021 02:05UTC+5.5	Shan_XD	447B - DZY Loves Strings	PyPy 3	Accepted	140 ms	

import string

#brute force
def stupid_strings(s,n,w):
    l = len(s)
    ans=0
    for i,v in enumerate(s):
        ans+=(i+1)*(w[string.ascii_lowercase.index(v)])
    for i in range(n):
        ans+=max(w)*(l + i + 1)
    #e = (l*(l + 2*n +1 )//2)*max(w)
    return ans





s=str(input())
n = int(input())
w = list(map(int,input().split()))
print(stupid_strings(s,n,w))
