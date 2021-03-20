#time limit exceed... but unique approach

s=str(input())
n=int(input())

def same_next(s):
    count=0
    while(s.find('##')>=0 or s.find('..')>=0):
        count+=s.count('..')+s.count('##')
        s=s.replace('..','.')
        s=s.replace('##','#')
    print(count)


for i in range(n):
    l,r = map(int,input().split())
    same_next(s[l-1:r])

















