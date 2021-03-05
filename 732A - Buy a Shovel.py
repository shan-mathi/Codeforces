#109169746	Mar/05/2021 22:33UTC+5.5	Shan_XD	732A - Buy a Shovel	PyPy 3	Accepted	108 ms	0 KB

k,r = input().split()
k=int(k)
r=int(r)
i=1
while((i*k-r)%10>0 and i*k%10>0):
    i+=1
print(i)
