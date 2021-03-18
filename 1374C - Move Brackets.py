#110284008	Mar/18/2021 11:55UTC+5.5	Shan_XD	1374C - Move Brackets	PyPy 3	Accepted	233 ms	5300 KB

def bracket_seq(n,brack):
    count=0
    while brack.count('()')>0:
        count+=1
        brack=brack.replace('()','',1)
    return(n//2-count)

t = int(input())
for i in range(t):
    n=int(input())
    brack=str(input())
    print(bracket_seq(n,brack))









