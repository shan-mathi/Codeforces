#117333902	May/25/2021 20:20UTC+5.5	Shan_XD	489C - Given Length and Sum of Digits...	PyPy 3	Accepted	109 ms	0 KB

import math

#brute force
def larg_smallest(m,s):
    if m*9 <s:
        return "-1 -1"
    if m==1 and s==0:
        return "0 0"
    if s<1:
        return "-1 -1"

    #largest
    l=''
    sl=s
    for i in range(m):
        if sl>=9:
            l+='9'
            sl-=9
        else:
            l+= str(sl)
            sl=0
    #smallest
    if l[-1]!='0':
        s = l[::-1]
        return (s+' '+l)
    s='1'
    count=0
    for i,v in enumerate(l[::-1][1:]):
        if v=='0':
            s+='0'


        elif v>'0':
            s+= str(int(v)-1) + l[::-1][i+2:]
            break
    return (s+' '+l)






m,s = map(int,input().split())

print(larg_smallest(m,s))









