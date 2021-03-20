#110510983	Mar/20/2021 12:41UTC+5.5	Shan_XD	327A - Flipping Game	PyPy 3	Accepted	248 ms	0 KB

n=int(input())
a = list(map(int,input().split()))

def coin_flip(n,a):
    count1=0
    count0=0
    extrmax0=-1
    n=n-1


    while (n>-1):
        if a[n]==1:
            count1+=1
            if count0>0:
                count0-=1
        else:
            count0+=1
            if count0>extrmax0:
                extrmax0=count0

        n-=1





    return count1+extrmax0

print(coin_flip(n,a))

















