#108303540	Feb/23/2021 18:59UTC+5.5	Shan_XD	546A - Soldier and Bananas	PyPy 3	Accepted	93 ms	0 KB

k,n, w= input().split()
k=int(k)
n=int(n)
w=int(w)
price= int(k*w*(w+1)/2 - n)
if price>0:
    print(price)
else:
    print(0)
