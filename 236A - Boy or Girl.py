#108302483	Feb/23/2021 18:51UTC+5.5	Shan_XD	236A - Boy or Girl	PyPy 3	Accepted	216 ms	0 KB

user = str(input())
user=[i for i in user]
len = len(set(user))
if len%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
