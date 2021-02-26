#108535831	Feb/26/2021 17:39UTC+5.5	Shan_XD	1030A - In Search of an Easy Problem	PyPy 3	Accepted	93 ms	0 KB

n=int(input())
x = list(map(str, input().split()))
x="".join(x)
if int(x)==0:
    print('EASY')
else:
    print('HARD')
