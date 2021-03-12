#109753377	Mar/12/2021 11:07UTC+5.5	Shan_XD	181A - Series of Crimes	PyPy 3	Accepted	218 ms	0 KB


n,m = input().split()
table = []
row = []
for i in range(int(n)):
 
    a=str(input())
    table.append(a)
    if a.find('*')>=0:
        row.append(i)
for i in range(int(m)):
    if table[row[0]][i]=='*' and table[row[1]][i]=='*':
        continue
    elif table[row[0]][i]=='*' and table[row[1]][i]!='*':
        print("{} {}".format(row[1]+1,i+1))
    elif table[row[0]][i]!='*' and table[row[1]][i]=='*':
        print("{} {}".format(row[0]+1,i+1))
