#113412924	Apr/18/2021 17:50UTC+5.5	Shan_XD	1359B - New Theatre Square	PyPy 3	Accepted	467 ms	6300 KB

def white_pavement(pav , x, y):
    nx=0
    ny=0

    for i in pav:

        sp = i.split('*')
        for j in sp:
            if len(j)%2==0:
                nx+= len(j)//2

            else:
                nx += len(j) // 2
                ny+=1
    return min((x*nx + y*ny), y*(2*nx + ny))




t = int(input())
for i in range(t):
    n,m,x,y = map(int,input().split())
    pav=[]
    for i in range(n):
        pav.append(str(input()))

    print(white_pavement(pav,y,x))



