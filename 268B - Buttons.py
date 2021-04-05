#112062998	Apr/05/2021 15:09UTC+5.5	Shan_XD	268B - Buttons	PyPy 3	Accepted	186 ms	1200 KB

n= int(input())
attempt=n
for i in range(1,n):
    attempt+= i*(n-i)
print(attempt)


