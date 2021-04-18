#113420549	Apr/18/2021 19:39UTC+5.5	Shan_XD	459A - Pashmak and Garden	PyPy 3	Runtime error on test 1	124 ms	2100 KB

import math
def square(x1,y1,x2,y2):
    p=[x1,y1]
    q=[x2,y2]
    d = math.dist(p,q)

    #3 conditons:
    # ify1 ==y2
    if y1==y2:
        l = abs(x2-x1)
        return("{} {} {} {}".format(x1,y1+l,x2,y1+l))
    elif x1==x2:
        l = abs(y1-y2)
        return ("{} {} {} {}".format(x1+l,y1,x2+l,y2))
    elif int(d/math.sqrt(2))== d/math.sqrt(2):
        return ("{} {} {} {}".format(x1,y2,x2,y1))
    else:
        return -1

x1,y1,x2,y2 = map(int,input().split())
print(square(x1,y1,x2,y2))






