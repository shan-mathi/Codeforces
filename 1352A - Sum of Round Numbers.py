#109085095	Mar/04/2021 19:28UTC+5.5	Shan_XD	1352A - Sum of Round Numbers	PyPy 3	Accepted	280 ms	4500 KB

t= int(input())
for i in range(t):
    n=str(input())
    ans=[]
    count=0
    for i in range(len(n)):
        if n[i]=='0':
            continue
        else:
            count+=1
            ans.append(str(int(n[i])*(10**(len(n)-i-1))))
    print(count)
    print(" ".join(ans))


