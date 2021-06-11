#119197302	Jun/12/2021 02:27UTC+5.5	Shan_XD	362B - Petya and Staircases	PyPy 3	Accepted	109 ms	1600 KB


def staircase(n,x):
    x.sort()
    if x[0]==1 or x[-1]==n:
        return False
    prev=1
    count=0
    for i in x:
        if i==prev+1 and count<3:
            count+=1

        elif i!= prev+1:

            count=1
        if count==3:
            return False
        prev = i
    return True


if __name__ == '__main__':
    n,m = map(int,input().split())
    if m==0:
        print('YES')
    else:

        x = list(map(int,input().split()))
        if staircase(n,x):
            print('YES')
        else:
            print('NO')

