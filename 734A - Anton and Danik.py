#108531954	Feb/26/2021 16:33UTC+5.5	Shan_XD	734A - Anton and Danik	PyPy 3	Accepted	93 ms	1800 KB

n=int(input())
games = str(input())
a=0
for i in games:
    if i=='A':
        a+=1
if a>len(games)-a:
    print('Anton')
elif a<len(games)-a:
    print('Danik')
else:
    print('Friendship')
