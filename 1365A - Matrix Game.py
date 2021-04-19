#113552070	Apr/20/2021 00:36UTC+5.5	Shan_XD	1365A - Matrix Game	PyPy 3	93 ms	2200 KB

import pandas as pd
def winner(n,m,data):
    df = pd.DataFrame(data)
    count=0
    for i in range(m):
        if df[i].sum()==0:
            for j in range(n):
                if df.loc[j].sum()==0:
                    df.loc[j,i]=1
                    count+=1
                    break

    if count%2==0:
        return 'Vivek'
    else:
        return 'Ashish'

t = int(input())
for i in range(t):
    n,m= map(int,input().split())
    data=[]
    for j in range(n):
        data.append(list(map(int,input().split())))
    print(winner(n,m,data))
