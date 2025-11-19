# class x:
#     def __init__(self,name):
#         self.name=name
#         print( self.name)
#     def __str__(self):
#         return "my name is : "+str(self.name)
#     def __add__(self,other):
#         obj=str(self.name)+str(other.name)
#         x4=x(obj)
#         return x4
# x1=x('satya ')
# x2=x('kaja ')
# x3=x('siva ')
# print(x1+x2+x3)

# method overloading:

# class x:
#     def m1(self):
#         print('1')
#     def m1(self,a,b):
#         print('2',a,b)
#     def m1(self,a):
#         print('3',a)
# obj=x()
# obj.m1()

# variable length argument:-
# --------------------------

# class x:
#     def m1(self,*x):
#         print(x)
# obj=x()
# obj.m1(1,2)
# obj.m1(1,2,3)
# obj.m1()

# default argument-
# ------------------
class x:
    def __init__(self,name):
        self.name=name
    def m1(self):
        self.name='aravind'
        print(self.name)
        x.a=10
x1=x('siva')
x1.m1()
print(x.a)        
    