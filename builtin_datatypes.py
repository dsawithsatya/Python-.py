#tuple is one of the builtin datatype in python 
# which we can declare between the "()" .It is immutable which we cant change the value.
#Let us perform some of the operations and methods using this tuple.
# It can acess the duplicate values because it is having index values.

t=("satya",1,"2004")
print()
print("Data type of the 't' is :",type(t))
print()
print(t)
print()
print("End of tuple declaration ")
print()
# Let us see how the duplicates can acess the tuple.

t1=("satya",1,2,"satya",2)
print()
print("datatype of t1 is : ",type(t1))
print()
print(t1)
print()
print("End of declaration of duplicate values :")
print()
# let us see how to access the tuple using index
print("===== Access the tuple values using index ====")
print()
print("print the 2nd index value from the tuple : ", t[2])
print()
print("end of aceess the values from tuple")
print()
# let us see how to access the tuple using negative index:
print("==== Access the tuple values using the negative index ==== ")
print()
print("Print the second index value of a tuple from T1 using -ve index :",t1[-3])
print()
print("end of access tuple using -ve index ")
print()
# let us see how to get set of collection from the tuple using start and end indexing:
print("Print the values from index 2 to 4 using start and end indexing :",t1[2:5])
print()
# same we can use -ve start and end index:
print("Print the values from index 2 to 4 using start and end -ve indexing :",t1[-3:])
print()
# Update the tuple values using the typecasting and then reassign to the tuple:
y=list(t1)
y[0]="Busireddy"
t1=tuple(y)
print("Print the tuple values after update ",t1)
print()
print(t1[0])

# append the values like what we have done before but here we are using the .append() function.
z=list(t)
z.append("satyanarayana")
t=tuple(z)
print("Print the values from the tuple after adding the values :",t)
# same as we can remove the values using the remove() function:
print()
y1=list(t)
y1.remove("satya")
t=tuple(y1)
print("Print the values after removing the value using remove() function :",y1)
print()

# add the two tuple using "+" :
th = ("satya", "kaja", "siva")
y = ("friends",) #"," is used to specify it is tuple not a string.
th += y
print("Print the values after add the two tuples",th)
print()

# unpack the values of a tuple using the variable assigning:
n=("satya",21,"student")
(name,age,occupation)=n
print("after assign a variables to the tuple words print 'satya' using name variable",name)
print()
print("age mention in the tuple :",age)
print()
print("Print the occupation of the tuple :",occupation)

#Loop tuples
tup=(1,2,2,4,5,5)
for i in tup:
    print(i)
print()
    
# for loop with range() and len ()function to print the values of a tuple:
for i in range(len(tup)):
    print(tup[i])
print()

# while loop using empty variable:
tupl=("satya","kaja","siva")
i=0
while i < len(tupl):
    print(tupl[i])
    i=i+1
print()
#join tuple values using '+':
a1=("satya",21,"student","full stack developer")
a2=("name",age,"occupation","course")
print(a1+a2)
#print(a1,"\n",a2)
print()

#tuple methods to perform 1.index() and 2.count()
# let us see how the index()function can work
iu=(1,2,33,3,3,2,3)
print("Index value of the given number ",iu.index(2))
print()
# also let us see how the count() function can work
print("count of the given number :",iu.count(3))
print()