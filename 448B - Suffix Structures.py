#119187391	Jun/11/2021 23:19UTC+5.5	Shan_XD	448B - Suffix Structures	PyPy 3	Wrong answer on test 19	93 ms	0 KB

def array(a,b):
    return sorted(a) ==sorted(b)

def automaton(a,b):
    p = 0
    l = len(b)
    for i in a:
        if p<l and i==b[p]:
            p+=1
    return p==l


def both(a,b):

    a = "".join(sorted(a))
    b = "".join(sorted(b))
    if a.find(b)>=0:
        return True
    else:
        return False
def main(a,b):
    if array(a,b):
        return 'array'
    elif automaton(a,b):
        return 'automaton'
    elif both(a,b):
        return 'both'
    else:
        return 'need tree'
if __name__ == '__main__':
    a = str(input())
    b = str(input())
    print(main(a,b))

