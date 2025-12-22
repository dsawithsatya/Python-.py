# class bank:
#     a=0
#     @staticmethod
#     def balance():
#         print("Your balance is : ",bank.a)
#     @staticmethod
#     def deposit():
#         x=int(input(" Enter the deposit amount : "))
#         bank.a+=x
#         print("afetr deposit your balance is : ",bank.a)
#     @staticmethod
#     def withdraw():
#         x=int(input("Enter withdraw amount : "))
#         if x<bank.a and x%100==0:
#             print("Withdraw suucessfull..")
#         else:
#             print("Enter correct amount ")
#         bank.a-=x
#         print("After withdrawal your balance is : ",bank.a)
# t=bank()
# while True:
#     print("Select your Bank Details .... ")
#     print()
#     print("========================================")
#     print()
#     print("1.Balance\n","2.Deposit\n","3.withdraw")
#     print()
#     print("=========================================")
#     e=int(input("select your query.... "))
#     if e==1:
#         t.balance()
#     elif e==2:
#         t.deposit()
#     elif e==3:
#         t.withdraw()
#     else:
#         print("Please select from the above options..\n")
#         break
#     print("Do u have any query.....yes/no \n")
#     x2=input("Enetr your answer..\n")
#     if x2=="yes":
#         pass
#     else:
#         break
# def a1(y):
#     def a():
#         y()
#         print('bye')
       
#     return a


# @a1       
# def x():
#     print('hi')
# x()

# x=10
# assert x!=10 ,'abc'
# print('bye')
# def a1(y):
#     def inner(name,phone_number):
#         if name.startswith('s') and len(phone_number)==10:
#             y(name,phone_number)
#     return inner


# @a1
# def x(name,phone_number):
#     print('sucessfull login')
    
# name=input('enter username')
# phone_number=input('enter username')
# x(name,phone_number)

# from abc import ABC,abstractmethod
# class x(ABC):
#     @abstractmethod
#     def m(self):
#         print('aa')
#     def m1(self):
#         print('bye1')
# class y(x):
#     def m(self):
#         print('bye')
# obj=y()

         
def x():
    for i in range(10):
        yield i
for i in x():
    print(i)
    
    