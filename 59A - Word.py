#108529047	Feb/26/2021 15:41UTC+5.5	Shan_XD	59A - Word	PyPy 3	Accepted	278 ms	0 KB

s=str(input())
upper=0
for i in s:
    if i >='A' and i<='Z':
        upper+=1
if upper>len(s)-upper:
    print(s.upper())
else:
    print(s.lower())
