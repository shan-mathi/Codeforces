#108304914	Feb/23/2021 19:10UTC+5.5	Shan_XD	791A - Bear and Big Brother	PyPy 3	Accepted	109 ms	0 KB

limak, bob = input().split()
limak = int(limak)
bob = int(bob)
count=0
while(limak <= bob):
    count+=1
    limak=limak*3
    bob= bob*2
print(count)
