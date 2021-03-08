#109421407	Mar/09/2021 00:03UTC+5.5	Shan_XD	802G - Fake News (easy)	PyPy 3	Accepted	109 ms	0 KB

news=str(input())
search='heidi'
pointer=0
ans='NO'
for i in news:
    if i==search[pointer]:
        pointer+=1
        if pointer==5:
            ans='YES'
            break
print(ans)
