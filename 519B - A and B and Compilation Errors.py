#110289601	Mar/18/2021 13:07UTC+5.5	Shan_XD	519B - A and B and Compilation Errors	PyPy 3	Accepted	420 ms	16700 KB

n=int(input())
l1 = list(map(int,input().split()))
l2= list(map(int,input().split()))
l3= list(map(int,input().split()))
l1.sort()
l2.sort()
l3.sort()
ans=[l1[-1],l2[-1]]

for i in range(n-1):
    if l1[i]!=l2[i]:
        ans[0]=l1[i]
        break
for i in range(n-2):
    if l2[i]!=l3[i]:
        ans[1]=l2[i]
        break
print(ans[0])
print(ans[1])













