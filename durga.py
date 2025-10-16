import math as m
from sys import argv
# Data type performing operations :
# Arithmetic operators using integers
any=10
print("Value",any)
print("Addition",any+any)
print("Sub",any-any)
print("Div",any/any)
print("Floor Div",any//any)
print("Mul",any*any)
print("Power",any**any)
print("Module",any%any)
print()

# Arithmetic operators using string==> + and *
# + ==> which can add the two strings.
# * ==> which can display multiple times
string="I am "
s1="satya "
print("1st String  :",string,"Second string",s1)
print(string+ s1)
print()
print("multiples of the string characters :", s1*3)
print()

# Using float values perform Arithmetic operations:
f0=11.5
f1=6.5
print("Float value 1 :",f0,"\nFloat value 2 :",f1)
print("Addition",f0+f1)
print("Sub",f0-f1)
print("Div",f0/f1)
print("Floor Div",f0//f1)
print("Mul",f0*f1)
print("Power",f0**f1)
print("Module",f0%f1)
print()

# checking bool values 
print()
print(bool(0 and 20))
print(bool(10 and 0))
print(bool(0 or 20))
print(bool(20 or 0))

#byte and byte array operations
a=[10,20,30,40]
b=bytes(a)
print(b)
for i in b: print(i)
print()

# data types - list, tuple, and set and some more data types:
# list - it can store the data using "[]", it is mutable:
l=[]
l.append(10)
l.append(20)
l.append(25)
l.append(50)
print("List of elements: ")
print(l)
print()
print("slicing operator :",l[0:4],l[3])
print()
# Tuple - it is same as list but it is immutable:
t=(10,20,30,40,50)
print("Tuple values : ",t[0:4])
#t.append(60)==> not possible 
print()
# declare the set of values using set:
# duplicates not allowed 
s={10,20,30,40,10}
print()
print("set values",s)
#range data type it can represent the sequence of values and it is immutable:
for i in range(0,100,10):print(i)
print()

# Relational operators :
# For int values  
r=10
r1=20
print()
print("value 1 :",r,"\nValue 2 :",r1)
if (r>r1):       #r<r1,r>=r1,r<=r1
    print("a is greater than b:",r)
else:
    print("b is gretaer than a:",r1)

print()

# for string values:
s2='a'
s3='A'
print(s2>s3) 
print(type(s2),type(s3))
print()

# Assignment operators:
# ==>compound operators Ex: a=10 then a+=10

x=10
x+=10
print(x)
y=15
y%=2
print(y)
x//=2
print(x)

# Ternary operator:
#syntax : x= 1st number if condition else 2nd number

p=20
z=30
q=10
min=20 if p<z and p<q else 30 if z<p and z<q else 10 
print("Minimum value of the given numbers: ",min)
print()
max=20 if p>z and p>q else 30 if z>p and z>q else 10
print()
print("Maximum Value of the given number :",max)
print()

# list Declaration
list=[10,25,30,45]
print()
print(list)
print()
#Acess with the indexing values
print("Printing the 2nd index value : ",list[2])
print()
# change the items in list using index:
list[1]=23
print("Changed 1st indexed value is :",list)
print()
# Add the items using append() method: 
list.append(20)
print("After adding the items :\n",list)
print()
# remove the items using remove() method:
list.remove(10)
print("print the list after removed the item",list)
print()
# loop the list using for loop it can print in one by one :
for i in list:
    print("After loop printing the values :",i)
    print()
print()
# comphenresive list that can take the another list to store data from the existing values:
l1=[]
for i in list:
    if i%2==0:
        l1.append(i)
print("Values in a list divisible by 2",l1)
print()
#Sort - it is used to sort the list of elements that is in numeric or alphabetical order:
print() 
list.sort
print("After sorting the elements in a list:",list)
print()

# join - using this we can join the data of a list:
o=["1","2","3"]
o1=["a","b","c"]
o2=o1+o
print("join the list data values :",o2)
print()
# copy() method is used to copy the data of a list into another list:
c=list.copy()
print("This is the copy of List values :",c)
print()
#pop() method is used to pop the data using the index value :
c.pop(1)
print("After removining the value using index :",c)
print()

#extend() is used to add the elements like an join method:
kaja=[11,23,25,17]
siva=[82,2,34,11]
kaja.extend(siva)
print("printing the values after extend the two lists :",kaja)
print()
 
kaja.insert(1,"satya")
print(" after adding the value using the insert method :",kaja)
print()

#print the values with special operators:
#Identity operator:
k=10
j=15
if k==j:
    print("satya")
else:
    print("Busireddy")
    
#Membership operator: ==> check the values in other variable
a1="Satya"
print("S" in a1)

#math module to perform the mathematics:
print(m.pi)
print()
print(m.sqrt(18))
print()
#bitwisw operators:
# this can applicable only for int and bool:
print(4 & 5)
print()
print(True and False)
print()
'''
#Input the 3 values from keyboard using eval() function:
a,b,c=(eval(x) for x in input("enter three numbers : ").split(" "))
print("The first value is :",a,"\n The second value is :",b,"\n The third value is :",c)
print()
'''
# Print the values from the range(4) also which can print from 1-3 only 
satya=""
for i in range (1,4):
    satya=str(i)+satya
print(satya)
print()
print("After changed the type ",int(satya))
print()
print(type(satya))
print()

#print the values from the command line :
# here we can use sys function and argv
print(argv[0:]) 
print()

# Is there any way to print the sum of the elements in a command line argument:
args=argv[1:]
sum=0
for i in args:
    sum1=int(i)
    sum=sum+sum1
print("sum of the Command line elements : ",sum)
print()
