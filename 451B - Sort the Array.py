#116674034	May/19/2021 21:33UTC+5.5	Shan_XD	451B - Sort the Array	PyPy 3	Accepted	187 ms	10700 KB

import math


def sort_the_array(n, x):
    ctrl=0
    r = x.copy()
    r.sort()
    if r==x:
        print('yes')
        print(1,1)
        return
    i=0
    while(i<n):
        if r[i]!=x[i]:
            b=i
            break
        i+=1

    ri = r.index(x[b])
    xi = x.index(r[i])
    xx = x[i:xi+1]
    xx.reverse()
    if r[i:ri+1]==xx and x[xi+1:]==r[ri+1:]:
        print('yes')
        print(b+1,xi+1)
        return

    else:
        print('no')
        return






n= int(input())
x = list(map(int, input().split()))
sort_the_array(n,x)
