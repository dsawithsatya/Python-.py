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
year=1900
if year%4==0  :            #also we didn't get for the 100 years and we can get the leap year of 400,800,...etc
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
    
#33
#check the discount >10000 means 30% discount, >5000 means 20% discount, >1000 means 10% discount finally <=1000 means no discount
amount=5100
if amount>10000:
    discount=amount *(30/100)
    print("Discount amount is ",discount)
elif amount>5000:
    discount=amount*(20/100)
    print("Discount amount is ",discount)
elif amount>1000:
    discount=amount*(10/100)
    print("Discount amount is ",discount)
else:
    print("No discount")

#34
#print the no. is amstrong or not :
x=153
x1=len(str(x))
z=0
for i in str(x):
    z+=int(i)**x1
print(z) 
if x==z:
    print(x," is amstrong number ")
else:
    print(x,"is not a amstrong number") 
    
#35
#print the no. is amstrong or not -- without using str() in loop
w=153
t=w
f2=0
f3=len(str(w))
while 0<w:
    f1=w%10
    f2+=f1**f3
    w=w//10

print(f2)  
if  t==f2:
    print(f2," is amstrong number ") 
else:
    print(f2," is not a amstrong number")

#36
#Print the elements in a string in a sequence:
a="satyanaryana"
for i in a:
    print(i)
    
#37
#Also we can print the set of characters in a word without using slice :
a="satyanarayana"
for i in range(4,10):
    print(a[i],end="")
print()

#38
#Reverse of a given string 
z1=""
for i in a:
    z1=i+z1
print("Reverse of a string is ",z1)  

#39
#In a statement reverse the single word :
a1="satya is python developer"
a2=a1.split(" ")
a3=3    #initially im just using 1, but also we can get from the user/keyboard also
s=''
for i in range(1,len(a2)):   
    if i==a3:
        for j in a2[i]:
            s=j+s
        a2.insert(a3,s)
        a2.pop(a3+1)
print()     
                 
print("After reverse of a single word the string is  : "," ".join(a2))
print()
#40
#In a statement delete  the middle element of the string 
k1="python full stack"
k2=k1.split()
k3=len(k2)//2
for i in range(1,len(k2)+1):
    if i==k3:
        k2.pop(i)
print("After deleted the item the string will be "," ".join(k2))
print()

#41
#print a particular string word in a sentence:
l1=["python","full","stack"]
y=2
for i in range(1,len(l1)):
    if l1[i]==l1[y]:
        print("The requested item is :",l1[y])
print()
#42
#count the particular character do u want to count that elements in a string:
b1="I am python or generative AI dev"
b2='a'  # bydefault im taking
c=0
for i in b1:
    if i == b2:
        c+=1
print(f"The count of the {b2} is {c} ")
print()

#43
#if the length of the string is odd means delete middle item otherwise delete two middle items:
d="Abdullah"
d2=len(d)//2
d3=""
for i in range(len(d)):
    if d2==i:
        d3=d[:d2-1]+d[d2+1:]
        print(d3)    

#44
#sum of first and last element in a list:
ll=[1,2,3,4,5]
for i in range(len(ll)):
    if i==len(ll)-1:
        print(ll[i]+ll[0])  
print()
#45
#print the number with single digit without use str:       
x=129
z=0
while 0<x:
    z=z*10+x%10
    x=x//10
while 0<z:
    x=z%10
    z=z//10
    print(x)
print()

#46
#use another way to delete the middle items in a string:
s1="satyan"
s2=len(s1)
s3=[]
for i in s1:
    s3.append(i)
if s2%2==1:
    s3.pop(s2//2)
else:
    s3.pop(s2//2)
    print(s3.pop((s2//2)-1))
print(s3)
#for i in range(len(s3)+1):
#    if s2%2==1:
#        if i==s2//2:
#            s3.pop(i)
#        else:
#            s3.pop(i)
#            s3.pop(i+1)
#print(s3)      

#47
#print the cricketer got the century or not
d={"kohli":123,"rohit":70,"klrahul":50}
for i,j in d.items():
    if j>=100:
        print(i,"Got the century",j)
    elif j>=50:
        print(i,"Got the Half century",j) 
    else:
        print("Below Half_century") 
print()
       
#48
#print the string is a anagram or not 
j1="abc"
j2="cab"
if sorted(j1)==sorted(j2):
    print("It is anagram ")
else:
    print("It is not a anagram")
print()   

#49
#print the number is amstrong or not using while:
x=153
y=len(str(x))
s=0
while 0<x:
    z=x%10
    s+=z**y 
    x=x//10
print(s)

#50
#check the no. is  palindrom of a number using while:
f=121
u=f
o=0
while 0<f:
    x=f%10
    o=o*10+x
    f=f//10
if o==u:
    print(o, "is a palindrom number")
else:
    print(o,"is not a palindrom number")
    
#51
#print the highest length word in a string 
t="Python full stack"
y=t.split(" ")
for i in range(1,len(y)+1):
    if len(y[i-1])>len(y[i-2]) and len(y[i-1])>len(y[i-3]):
        print("Greater len word is  ",y[i-1])

#52
#print every digit in a number using while:
r=1297
char=0
while 0<r:
    char=char*10+r%10
    r=r//10
while 0<char:
    r=char%10
    char=char//10
    print(r)
print()
#53
#print the fibnocci sequence of a numbers using the swap numbers:
a,b=0,1
print(a)
for i in  range(6):
    a,b=b,a+b
    print(a)
print()

#54
#remove the spaces b/w the words 
e="python     full     stack"
y=e.split()
for i in range(len(y)):
    if y[i]==" ":
        y.pop(i) 

print(" ".join(y))

#55
#print the list of elements divisible by a number or not:
g=[7,9,11,14,21,19,28]
s=7
d=[]
for i in g:
    if i%s==0:
        d.append(i)
print()

#56
#print the set of elements which is even numbers in a list:
v=[1,2,3,4,5,6,7]
s=0
for i in v:
    if i%2==0:
        s+=i
print("The sum of even numbers is ",s)

print()

#57
#from above we can use range() and len() function:
v=[1,2,3,4,5,6,7]
s=0
for i in range(len(v)):
    if i%2==0:
        s+=i
print("The sum of odd numbers is ",s)
print()


#58
#Print the odd numbers sum in a list:
v=[1,2,3,4,5,6,7]
s=0
for i in v:
    if i%2==1:
        s+=i
print("The sum of odd numbers is ",s)
print()

#59
#from above we can use range function also:
v=[1,2,3,4,5,6,7]
s=0
for i in range(len(v)):
    if v[i]%2==1:
        s+=i
print("The sum of odd numbers is ",s)
print()


#60
#print hi if the character is there else print bye:
v="Python full stack"
z="s"
for i in v:
    if z in i:
        print("Hi")
    else:
        print("Bye")
        
#61
#print the list of elements using concatination
x=['a','b','c']
x1=''
for i in x:
    x1+=i
    
print(x)
print()

#62
#print the list of elements in a matrix way
l1=[[1,2,3],[4,5,6],[7,8,9]]
for i in l1:
    for j in i:
        print(j,end=" ")
    print()
print()

#63
#print the 5x5 * box using for loop;
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
print()
   
#64
#print the right side triangle:
for i in range(6):
    print("* "*i,end=" ")
    print()

print()
#65
#print the down right side triangle:

for i in range(6):
    if i==4 or j==4:
        print("* "*(5-i),end=" ")
    else:
        print(" ",end=" ")
    print()
print()


#66
#print the even elements using odd number condition:
for i in range (1,11):
    if i%2==1:
        continue
    print(i)
        
#67
#break the loop if the num is even:
for i in range(1,10,3):
    if i%2==0:
        break
    print("The numbers are",i)
print()
#68
#pass if the condition is not usefull:
for i in range(1,10):
    if i%2==0:
        pass
    print(i,end=" ")
print()
print()

#69
#Take the list of elements and check with the condition and continue:
h1=[1,2,"satya",5,7,8]
for i in h1:
    if i=="satya":
        continue
    print(i,end=" ")
print() 

#70
#print the highest characters word in a list or a string :
h2=["satya","narayana","sattya1432"]
for i in range(len(h2)):
    if len(h2[i-2])>len(h2[i-1]):
        print("Highest characters are ",h2[i-2])

#71
#print the list of elements in reverse without slicing or reverse function:
h4=[9,3,5,6,3]
for i in range(len(h4)):
    #h3.insert(1,h4[i-len([h4])])
    h4[i],h4[i-1]=h4[i-1],h4[i]
    print(h4)

#72
#same list can u print in desc order or asc order
# h5=[]
# for i in range(len(h3)+1):
#     if h3[i-1]<h3[i]:
#         h5.append(h3[i])        
# print("Ascending order of the list is ",h5)   
            