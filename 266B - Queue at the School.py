#108530221	Feb/26/2021 16:01UTC+5.5	Shan_XD	266B - Queue at the School	PyPy 3	Accepted	186 ms	0 KB

n,t= input().split()
q = str(input())
for i in range(int(t)):
    q=q.replace('BG','GB')
print(q)
