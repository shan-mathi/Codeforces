#110958070	Mar/25/2021 14:12UTC+5.5	Shan_XD	1335C - Two Teams Composing	PyPy 3	Runtime error on test 1	249 ms	10000 KB

from statistics import mode

def uniq_team(n,x):
    if n==1:
        return 0
    x.sort()
    if x.count(mode(x))<len(set(x)):
        return x.count(mode(x))

    else:

        teamA = [x[0]]
        teamB = []
        freq = 0
        for i in range(1,n):

            if x[i]==x[i-1]:
                freq+=1
            else:
                teamA.append(x[i])
                if freq>0:
                    teamB.append(freq)
                    freq=0
        if freq>0:
            teamB.append(freq)

        return min(len(teamA),max(teamB))

t = int(input())
for i in range(t):
    n=int(input())
    x= list(map(int,input().split()))
    print(uniq_team(n,x))



