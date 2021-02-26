#108533146	Feb/26/2021 16:53UTC+5.5	Shan_XD	677A - Vanya and Fence	PyPy 3	Accepted	109 ms	0 KB

n,h = input().split()
x = list(map(str, input().split()))
ans=len(x)
for i in x:
    if int(i)>int(h):
        ans+=1
print(ans)
