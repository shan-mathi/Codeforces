#108531660	Feb/26/2021 16:27UTC+5.5	Shan_XD	41A - Translation	PyPy 3	Accepted	248 ms	

ber=str(input())
bir=str(input())
ans='YES'
for i in range(len(ber)):
    if ber[i]!=bir[-i-1]:
        ans='NO'
        break
print(ans)
