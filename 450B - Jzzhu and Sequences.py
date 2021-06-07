#118709383	Jun/07/2021 15:33UTC+5.5	Shan_XD	450B - Jzzhu and Sequences	PyPy 3	Accepted	156 ms	0 KB

def reverse_fibonacci_m1(a,b,n):      #using pattern repetiotn
    s=[a,b,b-a, -a, -b, a-b]
    mod = int(1e9 + 7)
    return (s[(n-1)%6]%mod + mod)%mod
    
def reverse_fibonacci_m2(x,y,n):    #using while loop
    if n==2:
        return y
    if n==1:
        return x
    if n==3:
        return y-x
    i =2
    while i<n:
        i+=1
        y,x = y-x,y

    #ans = reverse_fibonacci(x,y,n-1) - reverse_fibonacci(x,y,n-2)
    return y-x
    
    
def reverse_fibonacci_m3(x,y,n):         #using recursive function    
    if n==2:
        return y
    if n==1:
        return x
    if n==3:
        return y-x
    ans = reverse_fibonacci(x,y,n-1) - reverse_fibonacci(x,y,n-2)
    return ans


x,y = map(int,input().split())
n = int(input())
print(reverse_fibonacci(x,y,n)%int(1e9+7))
