#108298489	Feb/23/2021 18:26UTC+5.5	Shan_XD	263A - Beautiful Matrix	PyPy 3	Accepted	218 ms	0 KB

matrix=[]
for i in range(5):
    x = list(map(str, input().split()))
    matrix.append(x)
for i in range(5):
    if '1' in matrix[i]:
        x=matrix[i].index('1')+1
        y=i+1
print(abs(3-x)+abs(3-y))
