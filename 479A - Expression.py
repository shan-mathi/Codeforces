#110096080	Mar/16/2021 14:43UTC+5.5	Shan_XD	479A - Expression	PyPy 3	Accepted	108 ms	

a=int(input())
b=int(input())
c=int(input())
ans=[]
ans.append(a+b*c)
ans.append(a*b+c)
ans.append(a*b*c)
ans.append(a+b+c)
ans.append((a+b)*c)
ans.append(a*(b+c))
print(max(ans))
