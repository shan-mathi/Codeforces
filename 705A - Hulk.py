#108536722	Feb/26/2021 17:54UTC+5.5	Shan_XD	705A - Hulk	PyPy 3	Accepted	93 ms	0 KB

n=int(input())
ans=''
for i in range(n):
    if i<n-1:
        if i%2==0:
            ans+='I hate that '
        else:
            ans+='I love that '
    else:
        if i%2==0:
            ans+='I hate it'
        else:
            ans+='I love it'
print(ans.strip())
