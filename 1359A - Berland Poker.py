#111274597	Mar/28/2021 16:06UTC+5.5	Shan_XD	1359A - Berland Poker	PyPy 3	Accepted	108 ms	1400 KB

t= int(input())

def poker(n,m,k):
    hands = n//k
    winning_hand = min(hands,m)
    m-=winning_hand
    sub=0
    if m//(k-1)>0:
        sub+=m//(k-1)
        if m%(k-1)>0:
            sub+=1
    elif m%(k-1)>0:
        sub+=1

    print(winning_hand-sub)




for i in range(t):
    n,m,k = map(int,input().split())
    poker(n,m,k)










