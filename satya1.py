# import os
# with open("satya1.txt","r+") as f:
#     print(f.tell())
#     text=f.write("satya is good ")
#     print(f.tell())

#     print(text)
#     f.seek(10)
#     print(f.tell())
#     print('bye')
# x=input("Enter ") 
# if os.path.isfile(x):
#     f=open(x,'r+')
#     f.seek(14)
#     f.write("satyanarayana\n")
#     f.write("Even numbers are :\n")
#     f1=[]
#     f2=[]
#     f3=[]
#     for i in range(20):
#         if i%2==0:
#             f1.append(str(i))
#         if i%2==1:
#             f2.append(str(i))
#         z=i*i
#         f3.append(str(z))
#     print(f.tell())
#     f.seek
#     a=' '.join(f1)
#     f.write(a+'\n')
#     print(f.tell())
#     b=' '.join(f2)
#     print("Current cursor position is :",f.tell())
#     f.write("Odd numbers are : \n")
#     f.write(b+'\n')
#     f.tell()
#     f.write("Squares of a numbers :\n")
#     f.tell()
#     c=' '.join(f3)
#     f.write(c)
    
    # f.seek(47)
    # for i in f1:  
    #     f.writelines(i) 
    #     print  
    
f=open("satya1.txt","r")
c=0
for i in f.readlines():
    a=i.split(" ")
    for j in a:   
        if "python" in j:
            c+=1
print(c) 
if "a" in "aeiou":
    print("hi")