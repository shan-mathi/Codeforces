#113804990	Apr/21/2021 23:48UTC+5.5	Shan_XD	1512D - Corrupted Array	PyPy 3	Time limit exceeded on test 4	2000 ms	9100 KB

def magic_subset(x,n):
    # we should take b-2 elements such that pne of the two remeving element will containg the sum of the rest.
    ans = x.copy()
    ctrl=[]

    for i in range(n):
        ctrl.append(x[i])
        for j in range(i+1,n):
            ctrl.append(x[j])
            summ = sum(x) - sum(ctrl)
            if summ==ctrl[0] or summ==ctrl[1]:
                ans.remove(x[i])
                ans.remove(x[j])
                ans = " ".join(str(x) for x in ans)
                return ans
            else:
                ctrl.pop(1)
        ctrl=[]
    return -1




t = int(input())
for i in range(t):
    n =int(input())
    x= list(map(int,input().split()))

    print(magic_subset(x,n+2))
