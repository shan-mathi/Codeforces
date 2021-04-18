#113430380	Apr/18/2021 22:03UTC+5.5	Shan_XD	1366A - Shovels and Swords	PyPy 3	Accepted	155 ms	2900 KB

def smith_game(s,d):

    count=0
    first_layer = min(s,d)
    extras = max(s,d) - first_layer
    if extras>= first_layer:
        return first_layer
    else:
        count += extras
        first_layer-=extras
    if first_layer%3==0 or first_layer%3==1 :
        count+=(first_layer//3)*2
    else:
        count+= (first_layer//3)*2 +1
    return count



t = int(input())
for i in range(t):
    s,d = map(int,input().split())
    print(smith_game(s,d))
