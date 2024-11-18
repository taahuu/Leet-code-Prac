r=[12, 35, 1, 10, 34, 1]


r.sort()
print(r)
a=r[-1]
print(a)
for i in range(len(r)):
    if a in r:
        r.pop()
print(r)
if len(r)==0:
    print(-1)
else:
    print(r[-1])
