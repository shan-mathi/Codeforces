#109080885	Mar/04/2021 18:33UTC+5.5	Shan_XD	141A - Amusing Joke	PyPy 3	Accepted	218 ms	0 KB

host = str(input())
guest =str(input())
pile = str(input())
total = host+guest
ans='YES'

if len(pile)==len(total):
    for i in total:
        if pile.find(i)==-1:
            ans='NO'
            break
        elif pile.find(i)>=0:
            pile = pile.replace(i,'',1)
else:
    ans='NO'
print(ans)
