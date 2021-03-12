#109758544	Mar/12/2021 12:31UTC+5.5	Shan_XD	169A - Chores	PyPy 3	Accepted	93 ms	1200 KB

n,p,v = input().split()
x= list(map(int,input().split()))
 
x.sort()
print(x[int(v)]-x[int(v)-1])
