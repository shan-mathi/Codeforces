#108532435	Feb/26/2021 16:41UTC+5.5	Shan_XD	271A - Beautiful Year	PyPy 3	Accepted	186 ms	0 KB

year=int(input())
year+=1
while(len(set(str(year)))<4):
    year+=1
print(year)
