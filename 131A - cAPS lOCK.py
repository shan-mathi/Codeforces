#110095374	Mar/16/2021 14:34UTC+5.5	Shan_XD	131A - cAPS lOCK	PyPy 3	Accepted	109 ms	0 KB

s = str(input())
if s==s.upper():
    print(s.lower())
elif s[1:]==s[1:].upper() and s[0]==s[0].lower():
    print(s[0].upper()+s[1:].lower())
else:
    print(s)
