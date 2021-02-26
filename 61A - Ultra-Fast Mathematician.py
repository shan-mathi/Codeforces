#108537755	Feb/26/2021 18:11UTC+5.5	Shan_XD	61A - Ultra-Fast Mathematician	PyPy 3	Accepted	108 ms	0 KB

n1=str(input())
n2=str(input())
ans=''
for i in range(len(n1)):
    ans += str(int(n1[i])^int(n2[i]))

print(ans)
