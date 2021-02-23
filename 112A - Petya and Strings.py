#108297353	Feb/23/2021 18:08UTC+5.5	Shan_XD	112A - Petya and Strings	PyPy 3	Accepted	218 ms	0 KB

str1 = str(input())
str2 = str(input())

str1 = str1.lower()
str2 = str2.lower()
a=0
for i in range(len(str1)):
    if str1[i]==str2[i]:
        continue
    elif str1[i]>str2[i]:
        a=1
        break
    elif str1[i] < str2[i]:
        a = -1
        break
print(a)
