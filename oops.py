# class A:pass
# class B:pass
# class C:pass
# class x(A,B):pass
# class y(B,C):pass
# class z(x,A,y,B,C):pass

# t=A()
# print(A.mro())
# p=B()
# print(B.mro())

# u=z()
# print("The order of the methods : ",z.mro())


# #Aggregation(HAS - a relation with weak bond)
# class Teacher:
#     def __init__(self,name):
#         self.name=name
# class school:
#     def __init__(self,school_name,t):
#         self.school_name=school_name
#         self.teacher=t
        
# t1=Teacher("Satya")
# t2=school("Ips school",t1)
# print(t2.school_name)
# print(t2.teacher.name)

# #composition(HAS a strong relation)

# class Engine:
#     def __init__(self):
#         print("Engine Created..")
# class car:
#     def __init__(self,brand):
#         self.brand=brand
#         self.engine=Engine()
# x=car("Ford.")
# print("Car brand is : ",x.brand)


# # method overriding :
# class QT_Request:
#     def Name(self,name):
#         self.name=name
#         print("Name is : ",self.name)
#     def Batch(self,batches):
#         self.batches=batches
#         print("Your from batch no. : ",self.batches)
# class MY_reponse(QT_Request):
#     def Name(self, name):
#         super().Name(name)
#     def Batch(self, batches):
#         self.batches=batches
#         print("I am from batch no : ",self.batches)
# qt=MY_reponse()
# qt.Name("satya")
# qt.Batch(50)



# #without passing the arguments method overriding:
# class x1:
#     def x(self):
#         print("My name is satya")
#     def x2(self):
#         print("my batch is 49")
# class x3(x1):
#     def x(self):
#         super().x()
#     def x2(self):
#         print("my batch is actually 50")
# t=x3()
# t.x()
# t.x2()


# #constructor overloading 
# class b:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def m1(self):
#         print(self.name)
#         print(self.age)
        
# class a(b):
#     def __init__(self,name,age,batch,id):
#         super().__init__(name,age)
#         self.batch=batch
#         self.id=id
#     def m1(self):
#         print()
#         print("My name is ",self.name)
#         print()
#         print("My age is ",self.age)
#         print()
#         print("My batch is ",self.batch)
#         print()
#         print(" My id is ",self.id)
#         print()
# x=a('satya',21,50,1076)
# x.m1()     
        
# n=5
# for i in range(0,n+1):
#     print(" "*(n-i),end=" ")
#     print()
#     for j in range(n,i-1,-1):
#         print((n-j),end=' ')
#     print()
                
# for i in range(5,0,-1):
#     print(" "*(i-1),end=" ")
#     for j in range():
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# print()

# x=1
# for i in range(5):
#     for j in range(i+1):
#         print(x,end=" ")
#         x+=1
#     print()
# print()

# x=0
# for i in range(5):
#     y=1
#     for j in range(i+1):
#         print(x+y,end=" ")
#         x+=1
#         y+=1
#     print()

# x=1
# for i in range(1,5):
#     for j in range(i):
#         print(x,end="")
#         x+=1

#     print()

# x = 1

# for i in range(1, 6):        
#     val = x
#     for j in range(i):       
#         print(val, end=" ")
#         val += 1
#     print()
#     x+= (i - 1)           


# x="101101100"
# y=""
# for i in x:
#     if i in "01":
#         y += i
# if x==y:
#     print("yes")
# else:
#     print("no") 
    

# print(bin(9032666106))
# x=1  
# for i in range(5):
#     for j in range(i+1):
#         print(i+1,end=" ")
       
# x='9'
# c=0
# for i in range(1,101):
#     for j in str(i):
#         if x==j:
#             c+=1
# print(c)


# x='5'
# y='7'
# z=x+y
# x=int(x)*2    #10
# x+=5    #15
# print(x)
# x*=5
# x+=int(y)
# x-=25
# if z==str(x):
#     print("Hi")

#encapsulation:
# class x:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def __m1(self):
#         print(self.a)
#         print(self.b)
# y=x()
# y._x__m1()   # for private method also we can use for variables as well

# def x2(x):
#     def inner(x1):
#         assert  len(x1)>=18 and x1[0] in 'sS','Please provide the character start with s and must be 18 characters'
        
#         return x(x1)
            
#     return inner
            
# @x2
# def x(x1):
#     print("you have entered the characters : ",x1)
    
# x(input("Enter the words : "))


# res=0
# for i in range(5):
#     res+=i
#     i+=5
# print(res)


# class bank:
#     b=[]
#     a={}
#     @staticmethod
#     def Add_student_details():
#         x=input("Enter your id : ")
#         y=input("Enter name : ")
#         bank.a["id"]=x
#         bank.a["name"]=y
#         bank.b.append(bank.a)
#     @staticmethod
#     def Display_students():
#         print("Your student details..",bank.b)
#         # print("afetr deposit your balance is : ",bank.a)
#     @staticmethod
#     def update_student_details():
#         if bank.a[id]==1:
#             pass
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
#     print("1.Add_students\n","2.Display_students\n","3.update_students\n","4.Delete_Students\n","5.Exit")
#     print()
#     print("=========================================")
#     e=int(input("select your query.... "))
#     if e==1:
#         t.Add_student_details()
#     elif e==2:
#         t.Display_students()
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

# x=[1,2,3,4]
# y=[]

# for i in range(len(x)):
#     s=0
#     for j in range(len(x)):
#         if i!=j:
#             s+=x[j]
#     y.append(s)
    
# print(y)

# x=[1,2,3,4,5,6,7]
# y=[]
# target=10
# for i in range(len(x)):
#    # for j in range(len())
#     if i<=len(x):
#         y.append(x[i])
#         x.pop(i)
#         if sum(x)-sum(y)==target:
#             print("Elements in x is : ",x," and elements in y is : ",y)
#             print("The sum of x is : ",sum(x),"\nsum of y is :",sum(y),"\nDifference is equal to target : ",target)


# import time
# from threading import *
# def x():
#     for i in range(10):
#         time.sleep(1)
#         print(i)
# def y():
#     for j in range(10):
#         time.sleep(1)
#         print(j)
    
# start=time.time()
# # t=Thread(target=x)
# t=x()
# t1=y()
# # t.start()
# end=time.time()
# print("Time taken is  ",end-start)

# class x:
#     def __init__(self,a):
#         self.a=int(input("Enter number "))
#         print(self.a)
# x(None)


# class x:
#     def __init__(self,a):
#         self.a=a
#         print(self.a)
# x(int(input("Enter number ")))

# class x:
#     def __init__(self):
#         self.a=10
#     def m1(self):
#         print(self.a)
#         for i in range(10):
#             print(i,end="  ")
# x()
# x().m1()

# class x:
#     @classmethod
#     def cls(cls):
#         print("Soda buddi")
# x().cls()

# class x:
#     @staticmethod
#     def m1():
#         print("Soda buddi : Pandi")
# x().m1()

# class cons:
#     def __init__(self):
#         self.a=10
#     def any(self):
#         print("soda buddi element is ",self.a)
#     @staticmethod
#     def static():
#         print("soda buddi kallu")
        
#     @classmethod
#     def soda(cls):
#         cls.b=20
#         print("The soda buddi element ",cls.b)
# obj=cons()
# obj.any()
# obj.static()
# obj.soda()
# cons.static()
# cons.soda()
