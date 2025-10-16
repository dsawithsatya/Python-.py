#let us write a python script using range() datatype and implement 15 use cases:
#1. Let us print the simple range of values :
#The range can be  declare in some forms  :
#let us start with the first form i.e, in the range we can give only end of the range, range must be (end-1) 

for i in range(10):
    #By default the start range is '0'
    print()
    print(i) #which can print the range of elements from 0-9
print()
for i in range(10):
    if i%2==0:
        print()
        print("Even numbers :",i)
print()
for i in range(15):
    if i%2!=0:
        print()
        print("Odd numbers :",i)

l=[1,2,3,4,5,6]
for i in range(len(l)):
    print()
    print("Print the range of the list:",i)# which can print the range of the list 
    print()
    
l=[1,2,3,4,5,6]
for i in range(len(l)):
    if l[i] in l:
        print()
        print("Print the index : ",i," and the value is : ",l[i])
print()

#2. also we can use form 2 we can give start and end range:
for i in range(1,10):
    print()
    #here the start will be 1
    print("After using range, print the values in range : ",i)# which can print the range from 1-9
print()

#We can store the range of elements in list 
l1=[]
for i in range(1,10):
    #Let me use for some operations which can print as a list
    l1.append(i)
print()
print(l1)
print()

#using range we can add the range values:
l1=0
for i in range(20,40):
    #Let me use for some operations which can print the addition of range values:
    l1+=i
print("Sum of the range values : ",l1)
print()

#Form 3, here we can use start,end(end-1),step(Which can escape the values):
# without using if condition we can get the even numbers in range uisng step value
l2=[]
for i in range(0,20,2):
    l2.append(i)
print("Even numbers using the step value : ",l2)
print() 

# without using the conditions we can print the odd numbers:

l3=[]
for i in range(1,20,2):
    l3.append(i)
print("Odd numbers using the step value : ",l3)
print()

#also we can use len(valriable) inside the range() for range of the values:

l4=[1,2,3,4,5,6,7,8]
for i in range(len(l4)):
    print("value from the list is : ",l4[i])
print()

l5=[5,6,7,8,1,2,3,4]
for i in range(0,5):
    print()
    print("value from the list using start and end is : ",l5[i])
print()

l6=[]
for i in range(0,8,2):
    l6.append(i)
print("Print the values of list using start,end, step values is :",l6)
print()

l7=[]    
for i in range(10,1,-1): #if step is negative end(end+1) will get from the range 
    l7.append(i)
print("List elements after reverse the range of values :",l7)
print()

l8=[]    
for i in range(-1,-5,-2): #if step is negative end(end+1) will get from the range 
    l8.append(i)
print("List elements after reverse the range of values using -ve start and end  :",l8)
print()

    

