l1=[1,2,3]
l2=l1
l2.append([1,2,3])
print()
print(l1)
print()
a=[1,2,3]
b=[1,2,3]
c=a
print(a==b)
print(a is b)
print(a is c)
print()
x=10
y=20
x+=y
print(x)
print()

for i in range(5):
    for j in range(5):
        if i==0 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(5):
    for j in range(5):
        if i==0 or j==4 or i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()
print()   
for i in range(5):
    for j in range(5):
        if i==4 or i==0 or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(4):
    for j in range(5):
        if j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
print()   
for i in range(5):
    for j in range(5):
        if i==0 or j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(3):
    for j in range(5):
        if j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
    
        

