#110102945	Mar/16/2021 16:17UTC+5.5	Shan_XD	466A - Cheap Travel	PyPy 3	Accepted	93 ms	0 KB

import math
n,m,a,b = map(int,input().split())
if m*a>b:
    sp= math.ceil(n/m)*b
    #compare sp*b and (n-(n//m)*m)*a+ (n//m)*b
    ps= (n-(n//m)*m)*a + (n//m)*b
    
    print(min(sp,ps))
else:
    print(n*a)
