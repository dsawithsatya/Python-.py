#1. print the mul of given string numbers
# a="4,5"
# x,y=a.split(",")
# p=int(x)*int(y)
# print("The value is -- ",p)  #o/p--20

#2.perform exclusive OR operator in 2 sets: not a comman values
# s1={1,2,3,4,5}
# s2={2,4,5}
# print(s1^s2)   #o/p--{1,3}

#3.which is valid for escape sequeces -- 1.\\,2.\n,3.\b,4.All of the above
# print("\\")
# print("\n")
# print("\b")
#o/p--All the Above

#4.use & operator to perform in list:
# l=[1,2,3,4,5]
# y=[i & 1 for i in l]
# print(y)  #o/p--[1,0,1,0,1]

#5.print the condition values using functions:
# s="full stack python"
# def a():
#     c={}
#     for stri in s:
#         c[stri]=c.get(stri,0)+1
#     for i in s:
#         if c[i]==1:
#             print(i)
#     print()
# a()  #o/p-- all the sigle elements can print

#6.Print the 
# def x(arr, target): 
#     a, b = 0, len(arr) - 1 
#     while a <= b: 
#         mid = (a + b) // 2 
#         if arr[mid] < target: 
#             a= mid + 1
#         elif arr[mid] > target: 
#             b = mid-1
#         else:
#             return mid 
#     return -1 
# print(x([1, 2, 3, 4, 5], 3))  #o/p--3


#7.check the items are list and print in a single list:
# def x(a):
#     y=[]
#     for item in a:
#         if isinstance(item,list):
#             y.extend(x(item))
#         else:
#             y.append(item)
#     return y
# print(x([1,[2,[3,4],5],6]))  #o/p--[1,2,3,4,5,6]


# 8)append the values using differnce function calling
# def func(x,y=[]):
#     y.append(x)
#     return y
# print(func(1)) #1
# print(func(2)) #[1,2]
# print(func(3,[]))#[3]
# print(func(4))#[1,2,4]

# 9)
# x=10
# def outer():
#     x=5
#     def inner():
#         nonlocal x
#         x+=1
#         return x
#     return inner
# f=outer()
# print(f(),f(),f())

# x=[[],[]]*2 
# x[0].append(1)
# print(x)


# 11)append the elements and compare the condition 
# nums=[1,2,3,4]
# for i in nums:
#     nums.append(i+10)
#     if len(nums)>6:
#         break
# print(nums)

# 12)using lambda function and comprehension
# s=[lambda :i*2 for i in range(4)]
# print(s)
# for i in range(len(s)):
#     print(s[i]())
    
#14)using enumerator
# letters=['a','b','c']
# for i,letter in enumerate(letters):
#     letters.append(letter.upper())
#     if i==1:
#         break
# print(letters)

# 15)
# def gen():
#     for i in range(3):
#         yield i 
# g=gen()
# for i in [0,1,2]:
#     for j in [0,1,2]:
#         print(i,j)


# for n in range(2,10):
#     for x in range(2,n): 
#         if n%x==0:
#             break
#     else:
#         print(n)


# for i in range(10):
#     if i==4:
#         print('c')
# else:
#     print(i)



# 17)using swith case
# def s(choice):
#     match choice:
#         case "start": print('hi')
#         case "stop" : print('bye')
#         case _: print('default value')
# s('stop')

# 18)remove even number in the list
# x=[101,20,40,3,9]
# for i in x:
#     if i%2==0:
#         x.remove(i)
# print(x)

# 19)
# class A:
#     def __iter__(self):
#         yield 1
#         yield 2
# a=A()
# for x in a:
#     print(x)
    
# 20)
# items=[1,2,3]
# for x in items:
#     items.append(x+3)
#     if x>3:
#         pass
# print(items)

#without count function print the duplicate values:

# x=[10,20,20,30,30,30,40]
# y=x

# z=[]
# for i in x:
#     c=0
#     for j in y:
#         if i == j:
#             c+=1
#         if c>1 and i not in z:
#             z.append(i)
# print(z)  

#with count function print the duplicate values 
# x=[10,20,20,30,30,30,40]
# y=[]
# for i in x:
#     if x.count(i)>1 and i not in y:
#         y.append(i)
# print(y) 

# x=[10,20,20,30,30,30,40]

# x1=list({i for i in x if x.count(i)>1})   
# print(x1)

#print the reverse of a word in sentence
# x="python full stack"
# y=x.split(" ")
# z=int(input("Enter your word index to be reverse : "))
# s=''
# for i in range(len(y)):
#     if  i==z:
#         for j in y[i]:
#             s=j+s
#         y.insert(i,s)
# y.pop(z+1)      
# print(y)


# l = [1, 2, 3, 4]

# n = len(l)
# for i in range(n):
#     for j in range(i + 1, n):
#         if i + j == n - 1:
#             l[i], l[j] = l[j], l[i]

# print(l)

