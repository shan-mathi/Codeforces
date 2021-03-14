#109971214	Mar/14/2021 18:01UTC+5.5	Shan_XD	58A - Chat room	PyPy 3	Accepted	93 ms	0 KB

s=str(input())
search='hello'
pointer=0
ans='NO'
for i in s:
    if i==search[pointer]:
        pointer+=1
        if pointer==5:
            ans='YES'
            break
print(ans)
