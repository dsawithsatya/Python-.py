'''
#check the number is palindrom number that is the reverse of a number is same as original :
#first get the remainder using '%' then add to the reverse then the reverse become as remainder value then multiply with 10
# it will continue upto the loop satisfy
i=input("Enter the number :")
forif=i
rev=0
for j in i:
    print(i)
    num=int(i)%10

    rev=rev*10 +num
    i=int(i)//10
print("After reverse of a number is : ",rev)
if rev==int(forif):
    print("The number is palindrom")
else:
    print("The number is not a palindrom")
    

#The code for checking the number is amstrong or not
# for that we need the length of the number then power with the every digit of the number then add all the powers
# if it will gives the same number as original then it is a amstrong number    
i1=input("Enter a number")
add=0
n=len(i1)
for i in i1:
    digit=int(i)
    add+=(digit**n)
print("After check the number ",add)
if add==int(i1):
    print("THE number is Amstrong number ")
else:
    print("The number is not a amstrong")  
'''   

#check the 1 and 0 then print the zero's at last:
x=[1,2,3,1,0,5,1,2,1,0,4,5,1,0,5,6,7]
for i in range(len(x)):
    if x[i]==0:
        if x[i-1]==1:
            x.append(x[i])
            x.pop(i)
print(x)
#check whether the number is prime or not:
e = int(input("Enter any number: "))
if e < 2:
    print("The number is not prime (prime numbers starts from 2 .")
else:
    for i in range(2, e):
        if e % i == 0:
            print(e," is not a prime number because it is divisible by",i)
            break
    else:
        print(f"{e} is a prime number because it is only divisible by 1 and itself.")        
        

          
j=[[1,2,3],[4,5,6],[7,8,9,]]
for i in j:
    for k in i:
        print(k," --- ",i)
    print()
       

for i in range(1,6):
    for j in range(1,6):
        print("* "*j)
    
    if i==1:
        break
for l in range(1,6):
        print("* "*l)
  
    
