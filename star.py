print()
for i in range(5):
    for j in range(5):
    # print("* "*i,end=" ")
    # print()
        if i==4 or j==0 or  i==j or j==i-1 or j==i-2:
        #if i==4 or j==0 or i==j or i==J+1 or i==j+2
        
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
l1=[1,2,3,4]
l2=[1,3,4]
l3=[1,4]
l4=set()
a=l1+l2+l3
for i in a:
    if a.count(i)==3:
        l4.add(i)
print(l4)  
print() 

for i in range(5):
    for j in range(5):
        if i==0 or j==4 or i==j or i==j-1 or i==j-2 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()     


for i in range(6):
    for j in range(5):
        if i==0 or j==0 or i==5 or j==4  or j==i-1 or j==i-2 or j==i-3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()


