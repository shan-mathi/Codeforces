#117268140	May/25/2021 02:34UTC+5.5	Shan_XD	507B - Amr and Pins	PyPy 3	Accepted	93 ms	

import math

#brute force
def stupid_geometry(r,x,y,x1,y1):
    d = ((x1-x)**2 + (y1-y)**2)**0.5
    return int(math.ceil(d/r/2))




r,x,y,x1,y1 = map(int,input().split())
print(stupid_geometry(r,x,y,x1,y1))










