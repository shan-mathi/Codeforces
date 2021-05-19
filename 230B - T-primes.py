#116676966	May/19/2021 22:05UTC+5.5	Shan_XD	230B - T-primes	PyPy 3	Time limit exceeded on test 36	2000 ms	16600 KB

import math
def T_prime(x):
    for i in x:
        c=math.sqrt(i)
        ans=None
        # we check if the number is  perfect square
        if int(c)==c and c!=1:
            #if yes then chekc if the root is a prime number
            for j in range(2,int(math.sqrt(c))+1):
                if c%j==0:
                    ans='NO'
                    break
            if ans:
                print(ans)
            else:
                print('YES')
        else:
            print('NO')




n= int(input())
x = list(map(int, input().split()))
T_prime(x)
