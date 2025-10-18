# Control statements : it is used to apllication business logic or control the application logics
#There are three types of control statements 1.Decision making statements, 2.Iterative and 3.Transfer Statements

#1. decision making statements having the set of statements : if,if-elif,if-else,if-elif-else,nested if statements let us build the logic 

#if statement:
#1
a=10
if a%2==0:
    print("Even number is ",a)
print()

#2
a1=3
if a%2==1:
    print("Odd number ", a)
# also we can use list of elements:
#3
a=[1,2,3,4,5]
for i in range(len(a)):
    if a[i]%2==1:
        print("odd numbers are ",a[i])

#4
# also we can use the tuple:
a=(1,2,3,4,5,6)
for i in a:
    if i%2==0:
        print("Even numbers ", i)

#5
#let us use string value as a number and check the no.is even :
a="120"
b=int(a)
if b%2==0:
    print(" the number is even")

#6
#let us check the two numbers are equal or not using if 
a=10
b=10
if a==b:
    print(a, "and ",b," are equal")

#7
#let us whether the character is present in the word or not :
a="abcd"
b="a"
if b in a:
    print("The ",b,"character is present at ",a)
    
#8
# check how many vowels are there and count:
a="my name is satya"
b=0
for i in a:
    if i in "AEIOUaeiou":
        print("Vowels are ",i)
        b+=1
print("Total vowels are ",b)

#9
#check the consonents of a given word:
a="Abdullah sir is teaching python"
c=0
for i in a:
    if i not in "AEIOUaeiou":
        print("Consonents are ",i)
        c+=1
print("The total consonents are ", c)

#10
#check the number is greater than other or not :
a=20
b=30
if a >b:
    print(a, " is greater than  ",b)
if b>a:
    print(b," is greater than ",a)
    
#11
#remove the duplicates in a list of elements using not in and print the values:
l=[1,2,3,4,1,2,3,4,1]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

#12
#check the number is between the 1 and 100 or not:
i=22
if i>=0 and i<=100:
    print(i, "is between 1 and  100")

#13
#check more conditions using if :
i=10
if i<10:
    print(i,"is less than the 10")
if i>10:
    print(i," is greater than the 10 ")
if i==10:
    print("The number is equal to 10 ")
    
#14
#Check the list and update with cart overload:
l=[1000,2000,100,3000,4000]
if sum(l)>10000:
    print("Cart is overload")
    
    
#15
#check the list of items and print item is already is there:
l=[1,2,4,5,1,6]
l1=[]
for i in l:
    if i not in  l:
        l1.append(i)
else:
    print("item already exist")  

#if-else statements : It checks the conditions and give the output based on requirements or else part can be print    
#16
#Using if-else print both the even and odd number within single code:
a=[1,2,3,4,5,6] 
for i in a:
    if i%2==0:
        print(i,"is Even number")
    else:
        print(i,"is odd number")
    print()
print()
#17
#using another condition to check the odd and print 
     
a=[1,2,3,4,5,6] 
for i in a:
    if i%2==1:
        print(i,"is odd number")
    else:
        print(i,"is even number")
    print()
print()

#18
#using the string the given number is palindrome or not:
a='123'
a1=''
for i in a:
    a1=i+a1
if a1==a:
    print(a1," is palindrome that is reverse of  ",a)
else:
    print(a1,"is not palindrom that iis not reverse of ",a)
    
#19
#using the int data check the number is palindrom or not:
z1=121
z2=0
for i in str(z1):
    z2=z2*10+int(i)
print(z2)
if z2==z1:
    print(z2," is a palindrom  that is reverse of ",z1 )
print()
#20
#using for print the square of a given number :
y1=10
if y1>0:
    print("square of a number is ",y1*y1)
print()

#21
#print how many digits and alphabets present in a string:
t1="1ab35"
d1=0
alp=0
for i in t1:
    if i.isdigit():
        d1+=1
    else:
        alp+=1
print("The digits count is ",d1)
print("The aplhabets are ",alp)  

#22
#print the range of elemets in single line:
for i in range(1,10):
    print(i,end=" ")
print()  
#23
#print the even numbers without using condition:
for i in range(0,101,2):
    print("The even numers are ",i)  
print()   


#24
#Also using same for loop we can print the odd numbers upto 100:
for i in range(1,100,2):
    print("The odd numbers are ",i)
print()

#25
#print the fibnocci sequence of numbers using for loop:
a,b=0,1
for i in range(10):
    print(a,end=" ")
    a,b=b,a+b
print()

#26
#print the specific term of the series --nth term of a series 
a,b=0,1
for i in range(10):
    if i==10-1:
        print("The specific term series",a)
    a,b=b,a+b
print()        

#27
# print the elements is present or not :
c1=[1,"Satya",23,"sir"]
if "Satya" not in c1:
    print(True)
else:
    print(False)
    
#28 
#print the character is present in the string or not :
s="my name is satya"
if "y n" in s:
    print("the character is present ")
else:
    print("Not yet present")
    
#29 
#check the colors is present in the set or not:
color={"red","blue","green"}
if "yellow" in color:          # we can choose from the keyboard as well and check the condition
    print("Color is present")
else:
    print("not present")
print()   
#30
#check the year is leap year or not :
year=1996
if year%4==0 or year%400==0 :            #also we didn't get for the 100 years and we can get the leap year of 400,800,...etc
    print("leap year")
else:
    print("not a leap year")
print()


#31
#print the account balance:
amount=10000
withdraw=2000
if withdraw>0:
    if withdraw<=amount:
        if withdraw%100==0:
            amount-=withdraw
            print("Transaction successful")
            print("Balance amount is ",amount)
        else:
            print("Enter amount based on divisible by 100")
    else:
        print("Insuffient balance")
else:
    print("Invalid amount")

#32
#check the login details :
user="admin"
password="1234"
if user=="admin" and password=="1234":
    print("Login successfully")
else:
    print("Enter valid user or password")