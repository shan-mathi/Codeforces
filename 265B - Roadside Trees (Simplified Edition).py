#118711536	Jun/07/2021 15:59UTC+5.5	Shan_XD	265B - Roadside Trees (Simplified Edition)	PyPy 3	Accepted	1620 ms	8900 KB

def tree_jump(tree,t):
    time=-1
    current=0
    for i in range(t):

            time += abs(tree[i]-current)+ 2
            current = tree[i]


    return time






t= int(input())
tree=[]
for i in range(t):
    tree.append(int(input()))
print(tree_jump(tree,t))
