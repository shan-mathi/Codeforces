#108533860	Feb/26/2021 17:05UTC+5.5	Shan_XD	136A - Presents	PyPy 3	Accepted	186 ms	0 KB

n=int(input())
x = list(map(str, input().split()))
ans=[]
for i in range(1,n+1):
    ans.append(str(x.index(str(i))+1))
print(" ".join(ans))
