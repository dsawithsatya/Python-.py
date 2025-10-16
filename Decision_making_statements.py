#control statements can be divided into 3 types, Decision making is the one of the control statements :
# Types of Decision making we can conclude using if,nested if,if else,if elif else:
# Now let us build the 10 meaningful use cases :
# Start with simple use case  ==> check the entered number is satisfty the condition or not :
#1.use_case
a=eval(input("Enter any number : "))
if (a>=0):
    print("The entered no. is greater then Zero ")
    print()
if(a<=0):
    print("The number is less than Zero")
print("End of checking number is satisfy the condition or not ")
print()

#2.use_case   
# let us check the entered no. is even or not :
if (a%2==0):
    print("The entered number is even number :",a)
    print()
print("End of checking the number is even or not")
print()

#3.use_case
# now check the number is odd or not 
if(a%2==1):
    print("The entered number is odd")
    print()
print("End of checking the no.is odd or not")
print()

#4.use_case
# let us use some complex use_cases that can check both numbers :

if (a%2==0):
    print("The entered number is even number : ",a)
    print()
if (a%2!=0):
    print("The entered number is not an even number ",a)
    print()
print("End the checking the number is even or not using two conditions")
print()
#5.use_case
#Also we can check the entered number is odd or not :    
b=eval(input("Enter the second number :"))
if(b%2==1):
    print("The number is odd ")
    print()
if(b%2!=1):
    print("The number is not a odd number ")
    print()
print("End of checking the number is odd or not with two conditions")
print()

#6.use_case
#using and operator check the conditons :
if (a>=0 and b>=0):
    print("The both entered number are greater than the zero")
    print()
print("End of checking the numbers are greater than Zero")
print()

#7.use_case
#also we can check that which number is greater than the other:
if (a>b):
    print(a," : is greater than the  ",b)
    print()
if(b>a):
    print(b," : is greater than the ",a)
    print()
print("End of the Condition")
print()

#8.use_case
#let us check with the string conditons 
c=input("Enter your name : ")
if(c=="satya"):
    print("Good to see you and welcome ",c)
if(c!="satya"):
    print("Enter your name correctly")
    print()
print("End of condition")
print()

#9.use_case
# check with the user_name and password :
d=input("Enter user_name :")
p=input("Enter the password :")
if (d=="satya_123"):
    print("The user_name is : ",d)
    print()
if (p=="1432"):
    print("The password is : ",p)
    print()
print("End of the condition")
print()

#10.use_case
# Do some calculation with conditios
a1=eval(input("Enter a number for calculations :"))
a2=eval(input("Enter a number for calculations :"))
if (a1//a2==0):
    print(a1," : is perfectly divisible by ",a2)
    print()
if (a1//a2!=0):
    print(a1," : is not perfectly divisible by ",a2)
    print()
print("End of the condition")
print()


#let us continue with the nested if conditions 
# for first use case let us take with example of student grades :

#1. check the number is divisible by both 2 and 3 

num = int(input("Enter a number: "))
if num % 2 == 0:
    if num % 3 == 0:
        print("The number is divisible by both 2 and 3 is : ",num)
print()
print("End of the checking condition that the number is divisible by both 2 and 3")
print()

#2. use_case
# it will check the age if it is above 18 as well as above 21 means it will show the person is eligible for vote as well as adult
age = int(input("Enter age: "))
if age >= 18:
    if age >= 21:
        print("Adult and eligible for all elections")
print()
print("End of checking the person is eligible for vote and adult ")
print()

#3.use_case
# using user name and password condition it will give login successfull
username = input("Enter username: ")
print()
password = input("Enter password: ")

if username == "satya":
    if password == "1432":
        print("Login Successful")
    if password != "1432":
        print("Enter a correct password")
if username != "satya":
    print("Enter a correct user_name")


#4.use_case
# check the student grade using nested if condition
marks = int(input("Enter marks: "))
print()
if marks >= 0:
    if marks >= 90:
        print("Grade: A")
        print()
    if marks < 90:
        if marks >= 75:
            print("Grade: B")
            print()
    if marks < 75:
        if marks >= 50:
            print("Grade: C")
            print()
    if marks < 50:
        print("Grade: Fail")
        print()

#5.use_case
# Check the year is leap year or not:
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
            print()
    
        if year % 400 !=0:
            print("Not a Leap Year")
            print()
    if year % 100 !=0:
        print("Leap Year")
        print()
if year %4 != 0:
    print("Not a Leap Year")
    print()

print("End of the checking the year is leap year or not ")




