#118706045	Jun/07/2021 14:53UTC+5.5	Shan_XD	454B - Little Pony and Sort by Shift	PyPy 3	Accepted	218 ms	

def one_shift(n,x):
    c = x.copy()
    c.sort()
    if c ==x:
        return 0

    set =0
    for i in range(n):
        if x[i+1] < x[i] and not set:
            set = 1
            if (x[i+1:] + x[:i+1])== c:
                return n-i-1
            else:
                return -1
        if x[i+1] < x[i] and set:
            return -1
    return n - i -1


n = int(input())
x = list(map(int, input().split()))
print(one_shift(n,x))
