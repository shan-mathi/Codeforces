#108785743	Mar/01/2021 14:32UTC+5.5	Shan_XD	144A - Arrival of the General	PyPy 3	Accepted	186 ms	

n = int(input())
x = list(map(str, input().split()))
x = [int(i) for i in x]
x_rev=x.copy()
x_rev.reverse()
if x.index(max(x))> (len(x)-1-x_rev.index(min(x))):
    print(x.index(max(x)) + x_rev.index(min(x_rev)) - 1 )
else:
    print(x.index(max(x)) + x_rev.index(min(x_rev)))
