#109964607	Mar/14/2021 16:33UTC+5.5	Shan_XD	118A - String Task	PyPy 3	Accepted	186 ms	0 KB

inp = str(input())
inp=inp.lower()
vowels=['a','e','i','o','u','y']
for i in vowels:
    inp= inp.replace(i,"")
str=""
for i in inp:
    str+="."+i
print(str)
