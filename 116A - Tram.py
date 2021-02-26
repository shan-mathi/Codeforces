#108528455	Feb/26/2021 15:30UTC+5.5	Shan_XD	116A - Tram	PyPy 3	Accepted	278 ms	1400 KB

n=int(input())
passengers=[]
current=0
for i in range(n):
    a,b= input().split()
    current=current + int(b)-int(a)
    passengers.append(current)
print(max(passengers))
