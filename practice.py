"""
#print how many "a" values present in a string
a="aaabcdacdd"
b=0
for i in a:
   if "a"==i:
       b=b+1
print()
print("No. of a characters are : ",b)
print()
'''
#print the set of values using 3 variables and N is used for condion(Print the sum of 3 variable != N) in a list using the set formula 
x = int(input())
y = int(input())
z = int(input())
n = int(input())
result=[[i,j,k] for i in range(x+1) 
                      for j in range(y+1) for k in range(z+1)
                      if i+j+k !=n]
print(result)

'''
#Print the 3 number in the first and 7 number at last in a list :
a1=[1,3,4,5,7,6,7,3,2,5]
a2=[int(x) for x in a1 if x ==3 ]
a3=[int(x) for x in a1 if x==7]
a4=[int(x) for x in a1 if x!=3 and x!=7]
result=a2+a4+a3
print(result)
print()
# check the value is not present in the list or not :
a1=[1,3,4,5,7,6,7,3,2,5]
x=eval(input("Enter a value: "))
if x in a1:
    print("The value is present in the list : ",x)
    print()
else:
    print("The value is not present in the list :", x)
    print()

# print the values of a list of elements with 1st values is less than 10 last values is greater than 10
l=[1,3,4,11,7,8,22,3,24,19]
l1=[x for x in l if x<=10]
l2=[x for x in l if x>=10]
result=l1+l2
print(sorted(result))
print()
"""
#list data type 7 examples with the use cases:
#add the values to the list using append:
# 1st use case in list
l3=[1,2,3,4]
l3.append(4)
print()
print(l3)
print()
print("End of 1st use case ")
print()

#add the two list data's using the list concatination:
#2nd use case in list 
l4=[1,2,3,4,5]
l5=[2,3,4,5]
l6=l4+l5
print("After add the two lists :",l6)
print()
print("End of 2nd use case")
print()

#change the values of a list using index :
#3rd use case in list
l7=[1,3,5,6,"satya"]
l7[-1]=7
print("After change the value the list will be:",l7)
print()
# also we can use +ve index value to change the values in a list:
l7[2]=3
print("After change the value the list will be:",l7)
print()
print("End of the 3rd use case")
print()

#pop the values using pop() function
#4th use case in list
l8=[1,2,3,4,5,6,7] # this is the list then remove the last element 
print("Before pop the list :",l8)
l8.pop()
print("After pop the values of a list: ",l8)
print()
print("Also we can pop the values using the index of a vlaue :",l8.pop(4))
print("End of the 4th use case")
print()

#we can use extend function for extend the values of a list:
#5th use case in list
l9=[1,2,3,4,5,6]
l0=[2,3,4,5]
l9.extend(l0)
print("Afetr extend the list of elements :",l9)
print()
print("Also we can extend the list of elements from l0 ")
l0.extend(l9)
print(l0)
print()
print("End of the 5th use case")
print()

#count the character in a list using the count method:
#6th use case in list 
l01=[1,2,3,4,5,5,2,2,3,4,2]
print("Count the value of '2' in a list ",l01.count(2))
print()
print("Also we can use for loop to count the values of a list")
print()
l02=[1,2,3,2,4,2,5,6,2,1]
c=0
for i in l02:
    if i==2:
        c+=1
print(" After using the for loop the count will be :",c)
print()

#let us find the index values using index method:
#7th use case
print("Let us check the index of value 2 :",l01.index(2))
print()

# also we can insert the values using the inser() method with index values and insertion value :
print("Let us insert the value using insert() method :",l01.insert(2,9))
print()
print("End of the 7th use case ")
print()

# now we can see about the tuple use cases using methods:
# 1st use case
'''
t=tuple(input("Enter a set of tuple values"))
#Check the insertion is preserved that means the i/p should be equal to o/p :
print("Check the i/p is equal is equal to o/p : ", t)
print()
print("End of the checking oepration")
'''

#2nd use case using the duplicate values:
t1=(1,2,3,2,4,3,1,4)
print()
print("Check the duplicates are allowed or not :",t1)
print()
print("End of the Checking duplicates are allowed or not")
print()

#3rd use case using the heterogenous objects 
t3=(1,"satya",21.0,True)
print()
print("Check the objects is heterogenous:", t3)
print()
print("End of storing the heterogenous objects in tuple data type ")
print()

#4th use case using the max method to get the max value from the tuple :
t4=(1,3,400,9,33,200,300)
print("The max value of the tuple using max() methid :",max(t4))
print()
#also we have another way to find the max in tuple:
t4=sorted(t4)
print("After sorted print the max value using -ve index :",t4[-1])
print()
print("End of the finding Max value ")
print()

#5th use case using min value using min() methid in tuple:
print("The min value to get using min() method in tuple ",min(t4))
print()
print("After sorted the tuple we can use +ve index to get min value :", t4[1])
print()
print("End of the min() method ")
print()

#6th use case using len() method to get the length of the tuple:
print("Length of the tuple using len() method :", len(t4))
print()
# also we can use for loop to get the length of the tuple:
t5=0
for i in t4:
    t5=t5+1
print("Length of the tuple using the for loop :",t5)
print()
print("End of the len() method ")
print()

#7th use case using the index value to get the index of a value:
print("To get the index of value using the index() method :", t4.index(3))
print()
print("End of the index() method")
print()

#flow contol statements using if,if-else,if-elif-else,if-elif:
#find the biggest number from 2 input numbers
a=eval(input("Enter a first number : "))
print()
a1=eval(input("Enetr a second number : "))
print()
if a>a1:
    print("'a' is greater number : ",a)
    print()
elif a1>a:
    print("'a1' is greater number : ",a1)
    print()

#print the biggest number from 3 numbers:        
a2=eval(input("Enter a 3rd number :"))
print()
if a>a1 and a>a2:
    print( a,"is greatrer than",a1,"and ", a2)
    print()
elif a1>a and a1>a2:
    print(a1,"is greater than",a,"and",a2)
    print()
else:
    print(a2,"is grater than",a,"and",a1)
    print()
print("End of the if-elif-else condition")
print()
    
#print the given number is between the 1 and 100:
# using if and else condition we can print:
c1=eval(input("Enter a number between the 1 and 100 : "))
print()
if c1>=1 and c1<=100:
    print("The given number ",c1,"is between the 1 and 100")
    print()
else:
    print("The number ",c1,"is not between the 1 and 100")
    print()
print("End of the if-else condition")
print()


        


