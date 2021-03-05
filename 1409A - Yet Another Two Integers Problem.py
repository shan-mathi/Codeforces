#109169084	Mar/05/2021 22:22UTC+5.5	Shan_XD	1409A - Yet Another Two Integers Problem	PyPy 3	Accepted	405 ms	6900 KB

n= int(input())
for i in range(n):
    a,b = input().split()
    dif = abs(int(a)-int(b))
    if dif%10==0:
        print(dif//10)
    else:
        print(dif//10+1)
