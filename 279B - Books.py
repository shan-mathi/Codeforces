#119198452	Jun/12/2021 03:09UTC+5.5	Shan_XD	279B - Books	PyPy 3	Accepted	342 ms	10300 KB

#here using sum(q) will increase the time complexity to o(n^3) so rather maintain a variable that accumulates the sum

from collections import deque
def books(T,x):
    q = deque()
    summ=0
    maxx=0
    for i in x:
        q.appendleft(i)
        summ+=i
        while summ>T:
            summ-=q.pop()
        maxx = max(maxx,len(q))
    return maxx





if __name__ == '__main__':
    n,T = map(int,input().split())
    x = list(map(int,input().split()))
    print(books(T,x))


