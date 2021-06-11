#119189241	Jun/11/2021 23:44UTC+5.5	Shan_XD	259B - Little Elephant and Magic Square	PyPy 3	Accepted	216 ms	0 KB

def magic_square(a):
    ans =[ row[:] for row in a]
    ans[0][0] = (sum(a[2]) + sum(a[1]) - sum(a[0]))//2
    ans[1][1] = (sum(a[2]) + sum(a[0]) - sum(a[1])) // 2
    ans[2][2] = (sum(a[0]) + sum(a[1]) - sum(a[2])) // 2
    return ans




if __name__ == '__main__':
    a = []
    for i in range(3):
        a.append(list(map(int,input().split())))
    ans = magic_square(a)
    for i in range(3):
        a0 = map(lambda x: str(x),ans[i])
        print(" ".join(a0))

