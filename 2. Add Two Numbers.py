l1 = [2,4,3]
l2 = [5,6,4]
l1=l1[::-1]
l2=l2[::-1]
print(l1)
print(l2)
a=0 
b=0

for i in l1:
    a= (a*10)+i
for i in l2:
    b= (b*10)+i
print(a,b)
s=a+b
print(s)
s=int(str(s)[::-1])
print(s)
