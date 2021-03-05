#109170134	Mar/05/2021 22:39UTC+5.5	Shan_XD	1367A - Short Substrings	PyPy 3	Accepted	124 ms	3000 KB

n=int(input())
for i in range(n):
    a=str(input())
    ans=a[0]
    for j in range(1,len(a),2):
        ans+=a[j]
    print(ans)
