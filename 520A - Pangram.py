#108788162	Mar/01/2021 15:09UTC+5.5	Shan_XD	520A - Pangram	PyPy 3	Accepted	108 ms	0 KB
n = int(input())
pan = str(input())
if len(set(pan.lower()))==26:
    print('YES')
else:
    print('NO')
