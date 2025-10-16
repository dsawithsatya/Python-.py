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
    