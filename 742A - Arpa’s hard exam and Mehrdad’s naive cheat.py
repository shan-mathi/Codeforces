#111272594	Mar/28/2021 15:32UTC+5.5	Shan_XD	742A - Arpa’s hard exam and Mehrdad’s naive cheat	PyPy 3	Accepted	93 ms	

n= int(input())
if n==0:
    print(1)
else:
    while(n>=5):
            temp=n//5
            n= temp + n%5

    if n==0:
        print(8)
    elif n==1:
        print(8)
    elif n==2:
        print(4)
    elif n==3:
        print(2)
    elif n==4:
        print(6)









