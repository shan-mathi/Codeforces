#109804490	Mar/12/2021 23:02UTC+5.5	Shan_XD	1399B - Gifts Fixing	PyPy 3	Accepted	218 ms	6700 KB

t= int(input())
for test in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    b = list(map(int, input().split()))
    tar_a = min(a)
    tar_b = min(b)
    count=0
    for i in range(n):
        temp=0
        if a[i]>tar_a:
            temp= a[i]-tar_a
        if b[i]>tar_b:
            temp=max(temp,b[i]-tar_b)
        count+=temp
    print(count)



