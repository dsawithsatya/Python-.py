'''
l=[1,0,1,2,3,1,0,3,2,5,1,0,2]
for i in range(len(l)) :
    print(i)
    if l[i-1]==1:
        if l[i]==0:
            l.pop(i-1)
            l.append(1)
print(l)

s=input("Enter a string: ")
x=0
for i in s:
    print("positive index is :",x,"negative index is :",x-len(s),"The value is :",i)
    print()
    #also we can use format method we can access the values:
    print("Positive index is :{} Negative index is {},The value is :{}".format(x,x-len(s),i))
    print()
    x+=1

# To print the vowels in a given list:
# v='aeiou' 
l=['a','b','c','d','e']
h=[]
# for i in v:
#     for j in l:
#         if i == j:
#             h.append(i)
# print(h)

for i in l:
    if i in 'aeiouAEIOU':
        h.append(i)
print(h)
'''  

a=[1,2,3,4,7,9,4,3,7,8,6]
for i in range(len(a)):
    if a[i]==3:
        a.pop(i)
        a.insert(0,3)
    elif a[i]==7:
        a.pop(i)
        a.append(7)
print(a)   

x=[9,3,4,5,6,7,8,9]
x1=0
for i in x:
    if i%2!=0:
        x1+=i
print(x1)
            