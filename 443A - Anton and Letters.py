#108786380	Mar/01/2021 14:42UTC+5.5	Shan_XD	443A - Anton and Letters	PyPy 3	Accepted	108 ms	0 KB

list = str(input())
if list=='{}':
    print(0)
else:
    list = (list[1:-1].split(','))
    list = [i.strip() for i in list]
    print(len(set(list)))
