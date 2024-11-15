s="1337c0d3"
l=['0','1','2','3','4','5','6','7','8','9',"-"]
a=0
if s[0]=='-':
    s=s[1:]
for i in s:
    if i in l:
        a=(a*10)+int(i)
    else:
        break
if s[0]=='-':
    a=a*-1

print(a)
