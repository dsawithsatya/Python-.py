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

x = 1

for i in range(1, 6):        
    val = x
    for j in range(i):       
        print(val, end=" ")
        val += 1
    print()
    x+= (i - 1)           


x="101101100"
y=""
for i in x:
    if i in "01":
        y += i
if x==y:
    print("yes")
else:
    print("no") 
    

print(bin(9032666106))       



    
    
