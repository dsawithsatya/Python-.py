from math import *
# x=[{'name':'satya','age':21}]
# x1={'name':"Hari babu",'age':25}
# x2={'name':"sai",'age':23}
# def update():
#     if x1['name']=='Hari babu':
#         x1['name']='satya'
#         print(x1)
#     # x.append(x1)
#     # x.append(x2)
#     x1.update(x2)
#     print(x1)
    
# update()

#calculator using functions:
# a=10
# b=20
# def add():
#     print("Addition is : ",a+b)
# def sub():
#     print("Substraction is : ",a-b)
# def mul():
#     print("Multiplication is : ",a*b)
# def div():
#     print("Division is : ",a/b)
# def power():
#     print("a Power b  is : ",a**b)
# def sina():
#     x=int(input("Enter a sin(number : )"))
#     print("Sin value of a : ",sin(x))
# def cosa():
#     y=int(input("Enter the cos(number) :"))
#     print("cos value of a : ",cos(y))
    
# def tana():
#     z=int(input("Enter the tan(number) : "))
#     print("tan value of a : ",tan(z))
# def loga():
#     l=int(input("Enter the log(number) : "))
#     print("log value of a : ",log(a))


# while True:
#     a=int(input("Enter 1st number : "))
#     b=int(input("Enter 2nd number : "))
#     print("Select the operations from the given options ")
#     print()
#     print("=================================================\n")
#     print(" 1.addition\n","2.Substraction\n","3.Multiplication\n","4.Division\n","5.Sin\n","6.Cos\n","7.Tan\n","8.log\n")
#     print("=================================================")
#     print()
#     x=int(input("Enter your choice "))
#     if x==1:
#         add()
#     elif x==2:
#         sub()
#     elif x==3:
#         mul()
#     elif x==4:
#         div()
#     elif x==5:
#         sina()
#     elif x==6:
#         cosa()
#     elif x==7:
#         tana()
#     elif x==8:
#         loga()
    
#     else:
#         break
    
#calculator using oops class:
class calc:
    @staticmethod
    def add():
        print("Addition is : ",a+b)
    @staticmethod
    def sub():
        print("Substraction is : ",a-b)
    @staticmethod
    def mul():
        print("Multiplication is : ",a*b)
    @staticmethod
    def div():
        print("Division is : ",a/b)
    @staticmethod
    def power():
        print("a Power b  is : ",a**b)
    @staticmethod
    def sina():
        x=int(input("Enter a sin(number : )"))
        print("Sin value of a : ",sin(x))
    @staticmethod
    def cosa():
        y=int(input("Enter the cos(number) :"))
        print("cos value of a : ",cos(y))
    @staticmethod
    def tana():
        z=int(input("Enter the tan(number) : "))
        print("tan value of a : ",tan(z))
    @staticmethod
    def loga():
        l=int(input("Enter the log(number) : "))
        print("log value of a : ",log(a))

while True:
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    print("Select the operations from the given options ")
    print()
    print("=================================================\n")
    print(" 1.addition\n","2.Substraction\n","3.Multiplication\n","4.Division\n","5.Sin\n","6.Cos\n","7.Tan\n","8.log\n")
    print("=================================================")
    print()
    x=int(input("Enter your choice "))
    if x==1:
        t=calc()
        t.add()
    elif x==2:
        t=calc()
        t.sub()
    elif x==3:
        t=calc()
        t.mul()
    elif x==4:
        t=calc()
        t.div()
    elif x==5:
        t=calc()
        t.sina()
    elif x==6:
        t=calc()
        t.cosa()
    elif x==7:
        t=calc()
        t.tana()
    elif x==8:
        t=calc()
        t.loga()
    
    else:
        break
    
        
    