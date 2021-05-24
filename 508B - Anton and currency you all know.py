#117264605	May/25/2021 01:07UTC+5.5	Shan_XD	508B - Anton and currency you all know	GNU C++17 (64)	Accepted	31 ms	300 KB

import string

#brute force
def excahnge_rate(n):
    ans=-1
    l = int(n[-1])
    ctl = None

    for i in range(len(n)-1):
        if int(n[i])%2==0 and int(n[i])<l:
            s=n[:i] + n[-1] + n[i+1:-1] + n[i]
            return int(s)
        elif int(n[i])%2==0:
            ctl = i
    if ctl!=None:
        s = n[:ctl] + n[-1] + n[ctl + 1:-1] + n[ctl]
        return int(s)

    return ans










n=str(input())
print(excahnge_rate(n))
