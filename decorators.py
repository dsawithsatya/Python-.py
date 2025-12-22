# #1.decorator
# #check with the condtion and get the functionality
import time
# def y(x):
#     def inner(name,reg_no):
#         marks=80
#         if reg_no==1:
#             print("Name is ", name)
#             print("Reg_no is ",reg_no)
#             print("Your marks are : ",marks)
#         else:
#             return x(name,reg_no)
#     return inner
# @y 
# def x(name,reg_no):
#     print("Name is ", name)
#     print("Reg_no is ",reg_no)
# x("satya",reg_no=1)

# #2
# #check the time taken to complete the function task

# def work_1(sum1):
#     def inner():
#         start=time.time()
#         sum1()
#         print("Time taken to end the task is : ",time.time()-start)
#     return inner

# @work_1
# def sum1():
#     sum(range(100000))

# sum1()

# print(time.time())
# print("my name is satya")
# print(max(range(100)))
# print(time.time())

#prime number
# for i in range(2,101):
#     x=1
#     for j in range(2,i):
#         if i%j==0:
#             x=0
#             break
#     if x:
#         print(i)
        
# x=[2,4,1,5,20,30,5]
# first=0
# second=0
# for i in x:
#     if i>first:
#         first,second=i,first
#     elif first >i>second:
#         second=i
# print(second)



# y=[1,2,3,4,5,6,7]  #sum of two numbers is target=10
# target=10
# for i in range(len(y)):
#     for j in range(i+1,len(y)):
#         if y[j]+y[i]==target:
#             print("Two values index is ",j,i)
            

#greatest without duplicates value            
# s="abbbccdw"
# x1=set()
# x=0
# r=0
# for i in range(len(s)):
#     while s[i] in x1:
#         x1.remove(s[i])
#         x+=1
#     x1.add(s[i])
#     r=max(r,i-x+1)
# print(r)


# s="accdw"
# x1={1}
# x1.remove(1)
# x=0
# r=0
# for i in range(len(s)):
#     if s[i] in x1:
#         x1.remove(s[i])
#         x+=1
#     x1.add(s[i])
#     r=max(r,i-x+1)
# print(r)

    
# x={1}
# x.remove(1)#x=set()
# y={}
# print(x)
# print(y)
# print(type(x))
# print(type(y))
    
# x=[1,2,3]
# y=[]

# #output:[6,3,2]
# for i in range(len(x)):
#     if i==0:
#         y.append(x[i+1]*x[i+2])
#     elif i==1:
#         y.append(x[i-1]*x[i+1])
#     elif i==2:
#         y.append(x[i-1]*x[i-2])
# print(y)

#nearest prime number :
# x=[]
# for i in range(2,):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c<=2:
#         x.append(i)
# z=int(input("Enter your number to get the nearest prime number "))
# for i in range(len(x)):
#     if x[i]>=z:
#         print(x[i-1])
#         break
    # if x[i]>=z:
    #     print(x[i])
        
    
    
# x=[1,2,3,9,(3,2,5)]
# x.append(40)

# print(x)
    

# x="abccc"
# a=0
# b=0
# c=0
# for i in range(x):
#     if i=="a":
#         a+=1
#     elif i=="b":
#         b+=1
#     elif i==c:
#         c+=1
#     else:
#         print(i)
# print("Count of a is : ",a)
# print("Count of b is : ",b)

# x="a2b3c4"
# y=""
# for i in range(len(x)):
#     if x[i].isdigit():
#         y+=int(x[i])*x[i-1]
# print(y)        

x="aabbcdeeee"
u=""
for i in range(len(x)):
    y=1
    if x[i-1]==x[i]:
        y+=1
        u+=x[i-1]+str(y)
print(u)       
        

# for i in x:
#     y=1
#     if i == "a":
#         y+=1
#         if y>=2:
#             u+=i+str(y)
#     else:
#         u+=i+str(y)
# print(u)       
        
               