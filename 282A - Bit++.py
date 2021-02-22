#108174054	Feb/22/2021 17:25UTC+5.5	Shan_XD	282A - Bit++	PyPy 3	Accepted	108 ms	0 KB

n= int(input())
x=0
for i in range(n):
    inp = input()
    if inp[:2] == '++' or inp[-2:] == '++':
        x+=1
    elif inp[:2] == '--' or inp[-2:] == '--':
        x-=1
print(x)
