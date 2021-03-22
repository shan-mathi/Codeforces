#110760412	Mar/22/2021 23:20UTC+5.5	Shan_XD	1343C - Alternating Subsequence	PyPy 3	Accepted	560 ms	18700 KB


def subseq_max_sum(n,s):
    ans=[]
    subset=[s[0]]
    for i in range(1,n):
        if s[i]*s[i-1]<0:
            ans.append(max(subset))
            subset=[]
        subset.append(s[i])

    ans.append(max(subset))

    print(sum(ans))


t= int(input())
for i in range(t):
    n= int(input())
    s= list(map(int,input().split()))
    subseq_max_sum(n,s)







