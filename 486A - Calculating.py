#108537342	Feb/26/2021 18:04UTC+5.5	Shan_XD	486A - Calculating Function	PyPy 3	Accepted	171 ms	0 KB

n=int(input())
func = lambda t: -1*(t**2)+(t)*(t+1)
if n%2==0:
    print(func(n//2))
else:
    print(func(n//2)-n)
