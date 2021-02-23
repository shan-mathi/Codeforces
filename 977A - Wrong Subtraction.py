#108305905	Feb/23/2021 19:17UTC+5.5	Shan_XD	977A - Wrong Subtraction	PyPy 3	Accepted	109 ms	0 KB

num, steps = input().split()
num = int(num)
steps = int(steps)

for i in range(steps):
    if num%10==0:
        num=num//10
    else:
        num-=1
print(num)
