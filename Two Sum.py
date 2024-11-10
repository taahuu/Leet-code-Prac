li=[]
for i in range(5):
    a=int(input(f"Enter number {i+1}:"))
    li.append(a)
target=int(input("enter the target:"))

print(li)
# print(len(li))

for i in range(len(li)):
    for j in range(i+1):
        if i==j:
            continue
        else:
            b =li[i]+li[j]
            if b==target:
                print(f"[{j+1},{i+1}]")
            