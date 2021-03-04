#109082098	Mar/04/2021 18:49UTC+5.5	Shan_XD	996A - Hit the Lottery	PyPy 3	Accepted	108 ms	0 KB

balance = int(input())
count=0
while(balance>0):
    if balance>=100:
        count=count+balance//100
        balance=balance%100

    elif balance>=20:
        count=count+balance//20
        balance=balance%20
    elif balance >= 10:
        count = count + balance // 10
        balance = balance % 10
    elif balance >= 5:
        count = count + balance // 5
        balance = balance % 5
    elif balance >= 1:
        count = count + balance // 1
        balance = balance % 1
print(count)







