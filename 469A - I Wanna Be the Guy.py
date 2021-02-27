#108597774	Feb/27/2021 15:38UTC+5.5	Shan_XD	469A - I Wanna Be the Guy	PyPy 3	Accepted	93 ms	0 KB

levels = int(input())
litX = list(map(str, input().split()))
litY = list(map(str, input().split()))
litX.pop(0)
litY.pop(0)

ans= litX+litY
ans = set(ans)
if len(ans)==levels:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
