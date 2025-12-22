# x=[1,2,3]
# print((x,)*2)

# for i in range(3):
#     for j in range(3):
#         print(j+1,end=" ")
#     print()
# for i in range(3):
#     print((str(i+1)+" ")*3)

# for i in range(3):
#     print((chr(65+i)+" ")*3)

# for i in range(3):
#     for j in range(3):
#         print((chr(65+j)+" "),end=" ")
#     print()
# for i in range(5):
#     print(str(5-i)*5)
# for i in range(5,0,-1):
#     print(str(i)*5)
# for i in range(3):
#     print((chr(64+3-i)+" ")*3)

# for i in range(3):
#     for j in range(3,0,-1):
#         print((str(j)+" "),end=" ")
#     print()
    

# for i in range(3):
#     for j in range(3):
#         print((str(3-j)+" "),end=" ")
#     print()

# for i in range(3):
#     for j in range(3,0,-1):
#         print(chr(64+j),end=" ")
#     print()

# for i in range(3):
#     for j in range(3):
#         print(chr(64+3-j),end=" ")
#     print()

# for i in range(3):
#     print((i+1)*"* ")
# for i in range(3):
#     for j in range(i+1):
#         print("* ",end=" ")
#     print()

# for i in range(3):
#     print((i+1)*str(i+1))

# for i in range(3):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()



#substring of a given string --> remove the duplicates
# x=input("Enetr a string")
# y=[]
# for i in x:
#     if i not in y:
#         y.append(i) 
# print("".join(y)) 

# Function to find the leaders in an array

# result = []
# arr = [16, 17, 4, 3, 5, 2]
# n=len(arr)
# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] < arr[j]:
#             break
#     else:
#         result.append(arr[i])
# for i in result:
#     print(i,end=" ")
    

 
    







# x=int(input("Enter list of elements : "))
# for i in range(len(x)):
#     if(x[i-1]<x[i]):
#         print(x[i])
# else:
#     print(i)
    
# x=[1,5,3,10,7]
# y=[]
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]<x[j]:
#             break
#     else:
#         y.append(x[i])
# for j in y:
#     print(j)

x=[1,2,4,5,7]
for j in range(len(x)):
    # for i in range(x[j]):
    #     if i not in x:
    #         print("missing element is ",i)
    #         break
    for i in range(1,x[j]):
        if i not in x:
            x.append(i)
            print("The missing values are : ",i)

                
