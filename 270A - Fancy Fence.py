#110170982	Mar/17/2021 17:49UTC+5.5	Shan_XD	270A - Fancy Fence	PyPy 3	Accepted	154 ms	0 KB

def fence_sides(theta):
    n= 360/(180-theta)
    if int(n)==n:
        return 'YES'
    else:
        return 'NO'

t= int(input())
for i in range(t):
    theta = float(input())
    print(fence_sides(theta))






