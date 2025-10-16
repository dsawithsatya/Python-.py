
'''
from sys import argv as a
print(a[1:])

for i in a[1:]:
    for j in range(1,int(i)+1):
        s*=int(j)
        print(s)
'''       
#let use the command line for access the data from the keyboard
#Now do the operation on CLA to find the factorial of a given set of numbers:
            
from sys import argv as a
l=[]
for j in a[1:]: 
    s1=1  # for every loop it must be start with 1
    for i in range(1,int(j)+1):  # intially the given number is string so we have to change type using typecast int() function
        s1*=i
    print()
    print("The factorial of ",i, "is equal to :",s1)
    l.append(s1) #which can append the numbers to the list
print()
print(l)
print()


# Now do the operation on CLA to find the sum of a given set of numbers:
s2=0
for x in a[1:]:
    s2=s2+int(x)
print("Sum of the list numbers is ",s2) 
print()
print("End of the sum operations ")

# Now do the operation on CLA to find the max values of a given set of numbers:
#for j1 in range(len(a[1:])+1):
    # print(j1)
    # if int(a[1])<int(a[j1+1]) or j1+1>=3:
    #     print("The number is ",a[j1+1])
    #     break
    #if int(a[1])>a[j1+1]:
    #    print("The number is highest number ",a[1])
    #else:
    #    print("The number is greater number ",a[1])

#Now do the operation on CLA to find the max values of a given set of numbers:  
#import sys
#x=sys.argv
c=0
for i in a[1:]:
    if int(c)<int(i):
        c=i
print("The highest number in the given list is :",c)
print()


#reverse of a list of elements:
#form 1 
k1=[]
print("The reverse of a  list is ",a[:0:-1]) 
print()
for i1 in a[1:]:
    k1.insert(0,i1)
print("Reverse of a given list is : ",k1)     
print()

#Now do the operation on CLA to find the max values of a given set of numbers:  

c1=0
for i in a[1:]:
    if int(c1)<int(i):
        c1=i
print("The smallest number in the given list is :",i)
print()
