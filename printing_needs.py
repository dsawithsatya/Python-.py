# x="a3bb2c2"
# s=""
# y=[]
# for i in x:
#     if i.isdigit():
#         s=s+"/"
#         y.append(int(i))
#     else:
#         s=s+i
# z=s.split("/")
# for i,j in zip(z,y):
#     print(i*j)
    
# for i in range(5):
#     for j in range(7):
#         if j==3-i or (i==0 &j==3) or j==i+3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()

rows = 7


# for i in range(1, rows + 1):

#     # 1. Leading spaces before the first star
#     for s in range(rows - i):
#         print(" ", end=" ")   # space logic

#     # 2. Print stars with internal gap
#     for j in range(i):
#         print("*", end="")           # print star
#         for gap in range(4):         # create the gap logically
#             print(" ", end="")       # no direct big spaces

#     print()  # next line

# for i in range(5):
#     print((chr(65+i)+" ")*5)

# for i in range(4):
#     print("*"*4)

# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()

# for i in range(4):
#     print("*"*i)

# for i in range(1,5):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# a=1      
# for i in range(5):
#     for j in range(i):
#         print(a,end=" ")
#         a+=1
#     print()
# a=1
# for i in range(5):
#     for j in range(i+1):
#         print(a,end=" ")
#         a+=1
#     a=a-1
#     print()