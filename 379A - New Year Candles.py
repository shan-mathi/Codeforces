#110106654	Mar/16/2021 17:07UTC+5.5	Shan_XD	379A - New Year Candles	PyPy 3	Accepted	93 ms	0 KB

a,b= map(int,input().split())
count=a
burn=a
while(burn>=b):
    count+=burn//b
    rem=burn%b
    burn=burn//b+rem
print(count)



