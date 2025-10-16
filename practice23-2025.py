"""
#logical operators are 'And' and 'or ' operators 
# Let us perform the operators in data types:
l=eval(input("Enter  first number :"))
l1=eval(input("Enter  second number :"))
l2=eval(input("Enter Third number :"))
if l>l1 and l>l2:
    print(l,"is greater than the ",l1,"and ",l2)

elif l2>l1 and l2>l:
    print(l2,"is greater than the",l1,"and ",l)

elif l>l1 or l>l2:
    print("The given number is greater than one number :",l)


elif l2>l1 or l2>l:
    print("The given number is greater then ")

else:
    print(l1,"is greater than the ",l,"and ",l2)
"""
'''
u_name=input("Enter the user name : ")
pwd=(input("Enter the password : "))
if (u_name=="satya@123" and pwd=="satya@123"):
    print("you are successfully login with u_name : ",u_name,"and ",pwd)

elif u_name!="satya@123"  and pwd!="satya@123":
    print("you entered the password and u_name wrong check the u_name : ",u_name,"and ","Password : ",pwd)
elif u_name!="satya@123"  or pwd!="satya@123":
    print("you entered the password or u_name wrong check the u_name : ",u_name,"or ","Password : ",pwd)
else:
    print("You are not Authorized person")

#give the no. of substrings with the index values :    
s=input("Enter a main string : ")
sub=input("Enter a sub string : ")
pos=-1
flag=False
n=len(s)
while True:
    pos=s.find(sub,pos+1,n)
    if pos==-1:
        break
    print("The substring found at :",pos)
if flag==False:
    print("Sub string not found")
    
#using count variable can give count of values:  
k=input("Enter a main string")
k1=input("Enter a sub string")
pos=-1
n=len(k)
count=0
flag=False
while True:
    pos=k.find(k1,pos+1,n)
    if pos==-1:
        break
    count+=1
    print("String found at index :",pos)
    print("Count of the items",count)
    flag=True
'''
"""
#which can print the median of the given list characters
x=eval(input("Enter a set of list characters : "))
mid=len(x)//2
if len(x)%2==1:
    print(x[mid])
else:
    print((x[mid-1]+x[mid])//2)

"""
import time
#Logical operator and, or, not
print(" Let us start to perform the logical operators ")
print("===================================================")
a=eval(input("Enter a number : "))
b=eval(input("Enter a second number :"))
print( a>5 and b<200)
print()
print(a<100 or b>200)
print()
print(not(a and b))
print()
time.sleep(1)
print("End of the logical operators ")
print()

#Ternary operator a= x if x>y else y

print(" Let us start to perform the ternary operators ")
print("===================================================")

n=a if a>b else b
print("Check the bigger number using the ternary operator b/w a and b is :",n)
print()
c=eval(input("Enter the third number :"))
n1= a if a>b and a>c else b if b>a and b>c else c
print("Check the bigger number using the ternary operator b/w a, b, and c is :",n1)
print()
time.sleep(1)
print("End of the Ternary operators")
print()

#Assignment operator +=,-=, *=, /=, //=
print(" Let us start to perform the Assignment operators ")
print("===================================================")


a+=10
print("Add the value using assignment operator '+=' is  : ",a)
print()
a-=10
print("subtract the value using assignment operator '-=' : ",a)
print()
a*=10
print("Mulitiply the value using assignment operator '*=' : ",a)
print()
a/=10
print("Divide the value using assignment operator '/=' : ",a)
print()
a//=10
print("Floor Division of the value using assignment operator '//=' : ",a)
print()
a%=10
print("Modular of the value using assignment operator '%=' : ",a)
print()
time.sleep(1)
print("End of the Assignment operator ")
print()

#Equality operator ==, !=
#check the data of the given datatype or any character is equal to the other datatype or character ex: a==b it checks a data is equal to b or not 

print(" Let us start to perform the Equality operators ")
print("===================================================")

d=1 # we can take any datatype is it may be list,tuple,string ,etc...
d1=1
if d ==d1:
    print("d and d1 both are equal ")
    print()
# also we can represent in the print() function directly which can give as bool data type:    
print(d==d1)
print()
# also we can use character to check the equality
if 1==d1:
    print(d," is represnt in the d1 variable both are same :",d1)
    print()
# let us take the string as datatype check the characters is present or not using equality operator:
d2="satya"
if "satya"==d2:  #note : if we want check the unique character means we have to use membership operator 'in' and 'not in'
    print("satya "," - The given sequence of characters is present in the d2 variable ") 
    print()

print("It can print the given characters is present in the variable characters or not : ","satya"==d2)
print()
# Then check with the != operator which is quite opposite to the '==' opertor 
e1="satya123"
if "satya"!=e1:
    print("The string is not present in the e1 : ",e1)
print()
print("It can print that the given characters is equal to the variable character or not : ","s"!=e1) # we can use directly to get the output using print() function
print()
time.sleep(1)
print("End of the equality operator")
print()

      

    