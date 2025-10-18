x="153"
x1=len(x)
sum=0
for i in x:
   sum=sum+int(i)**x1
print(sum)
if sum==int(x):
    print("The number is amstrong ")
else:
    print("Not a amstrong")
    
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    for j in i:
        print(j,end=" ")
    print()

l1=["a","b","c",1,2,3,9.3,2.6]
l2=[]
for i in l1:
    if type(i)== str:
        print("string characters are ",i)
    elif type(i)==int:
        print("The int characters are ",i)
    elif type(i)==float:
        print("The float characters are ",i)
    
for i in l1:
    if isinstance(i,str):
        print("The string elements are ", i)
    if isinstance(i,int):
        print("The string elements are ", i)
    if isinstance(i,float):
        print("The string elements are ", i)
        
x="123abc"
for i in x:
    if i.isdigit():
        print("The digitvalue is ",i)
    if i.isalpha():
        print("The stringvalue is ",i)


#print the character of the instance after the number
a="a2b3c5"
for i in range(0,len(a),2):
    if isinstance(a[i],str):
        print(a[i]*int(a[i+1]))
'''        
b=list(input("Enter list of elements : "))
y=[]
z=0
while z<len(b):
    if b[z] not in y :
        y.append(b[z])
        print((b[z]).split(" "))
    z+=1
print(y)    
'''


for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4 :
            print("X",end=" ")
        else:
            
            print(" ",end=" ")
    print()

print()
print()  
 
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==2 :
            print("X",end=" ")
        else:
            
            print(" ",end=" ")
    print()
print()
print()        

for i in range(9):
    for j in range(5):
        if i==0 or i==4 or i==8 or j==0 or j==4 :
            print("X",end=" ")
        elif j==1 or j==2 or i==3:
            print(" ",end=" ")   

        else:
    
            print(" ",end=" ")
    print()

a1=[10,20,30,40,40,30,9,3,19]
a11=[]
for i in a1:
    if i%2==0:
        a11.append(i)
print(a11)
        
a2="python full stack"
a22=[]
for i in a2:
    if i in "aeiouAEIOU":
        a22.append(i)
print(a22)

a3=[10,20,30,10,20,20,30,40]
a4=[]
for i in a3:
    if i not in a4:
        a4.append(i)
print(a4) 

a5=[10,20,10,20]
a6=[]
for i in a5:
    if i not in a6:
        a6.append(i)  
print(a6)

rev="python full stack"
x3=rev.split()
mid=len(x3)//2
l4=""
for i in x3[mid]:
    l4=i+l4
x3.insert(mid,l4)
x3.pop(mid+1)
print(x3)
print("  ".join(x3))


rev="python full stack"
x3=rev.split()
mid=len(x3)//2
l4=""
for i in x3[mid]:
    l4=i+l4
x3.insert(mid,l4)
x3.pop(mid+1)
print(x3)
print( "  ".join(x3))
print()


for i in range(4):
    for j in range(7):
        if i==3 or  (i==2 and j==1) or (i==3 and j==5) or (i==2 and j==5) or (i==1 and j==4) or (i==0 and j==3) or (i==1 and j==2):
            print("X",end=" ")
        else:
            
            print(" ",end=" ")
    print()
print()
print()   


for i in range(4):
    for j in range(5):
        if i==3 or j==0 :
            print("X",end=" ")
        else:
            print(" ",end="")
            
    print()
print()
print()   

for i in range(6):
    for j in range(6):
            print("X",end=" ")
        
    print()
print()
print()        
     

for i in range(5):
    for j in range(5):
        if i==0  or j==0 or j==4 or i==4 :
            print("X",end=" ")
        else:
            
            print(" ",end=" ")
    print()
print()
print() 
 

for i in range(5):
    for j in range(5):
        if i==j or i==4-j:
            print("X",end=" ")
        else:
            
            print(" ",end=" ")
    print()
print()
print() 


for i in range(4):
    for j in range(5):
        if i==0 or i==1+j or i==5-j:
            print("X",end=" ")
        else:
            
            print(" ",end=" ")
    print()
print()
print()  


for i in range(5):
    for j in range(9):
        if j==4 or i==4-j  or i==4 or j==4+i :
            print("X",end=" ")
        else:
            
            print(" ",end=" ")
    print()
print()
print()        
      
       
      
  
