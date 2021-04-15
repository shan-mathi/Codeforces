#113056449	Apr/15/2021 09:37UTC+5.5	Shan_XD	133A - HQ9+	PyPy 3	Accepted	216 ms	

code = ['H','Q','9']
s = str(input())
s = (set(s))
ctr=0

for i in s:
    if i in code:

        ctr=1
        break
if ctr:
    print('YES')
else:
    print('NO')
