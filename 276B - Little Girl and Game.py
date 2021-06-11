#119196378	Jun/12/2021 01:59UTC+5.5	Shan_XD	276B - Little Girl and Game	PyPy 3	Accepted	218 ms	300 KB

from collections import Counter
def game(s):
    s_map = Counter(s)
    odd = 0
    for i in s_map:
        if s_map[i]%2==1:
            odd+=1
    if odd>1:
        return odd-1
    else:
        return 0

if __name__ == '__main__':
    s = str(input())
    ans = game(s)
    if ans%2==0:
        print('First')
    else:
        print('Second')




