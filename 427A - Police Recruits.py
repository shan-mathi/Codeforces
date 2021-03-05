#109170732	Mar/05/2021 22:48UTC+5.5	Shan_XD	427A - Police Recruits	PyPy 3	Accepted	124 ms	7600 KB

n=int(input())
events=list(map(int,input().split()))
police=0
crimes=0
for i in events:
    if i>0:
        police+=i
    else:
        if police>0:
            police-=1
        else:
            crimes+=1
print(crimes)
