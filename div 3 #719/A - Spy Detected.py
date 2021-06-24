#120434961	Jun/24/2021 16:04UTC+5.5	Shan_XD	A - Spy Detected!	PyPy 3	Accepted	108 ms	1800 KB

from collections import Counter
#brute force
def spy_detected(x):

    c = Counter(x)
    for i in c:
        if c[i]==1:
            p =i
            break
    return x.index(p)




t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    print(spy_detected(x)+1)








