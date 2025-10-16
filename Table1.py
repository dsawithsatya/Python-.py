"""x=int(input("enter a table number :"))
for i in range (1,11):
    print(x,"x",i,"=",x*i)


# check the percentage of the student marks :
a=eval(input("Enter the list of marks for 6 subjects : "))
sum=0
for i in a:
    if i >= 50:
        print(" You Pass This Exam , And marks will be ", i)
    else:
        print(" You Failed this Exam , Marks will be ", i)
    sum+=i
print(sum)
if (sum//len(a)) >= 90:
    print("The Grade is A +")
elif (sum//len(a)) >= 90:
    print("The grade is A")
elif (sum//len(a)) >=70:
    print("The Grade is B")
elif (sum//len(a)) >= 60:
    print("The Grade is c")
elif (sum//len(a)) >= 50:
    print("The Grade is D ")
else:
    print("The Grade is F, He failed the exam")

"""
    
x1=list(input("Enter a string : "))
x2=len(x1)//2
if len(x1) %2 ==0:
    print(" If even means pop item is ", x1.pop(x2),x1.pop(x2-1))
else:
    print("If odd means pop item is :",x1.pop(x2))
    
print("The remaining string is ","".join(x1))
print(x2)    

x3=eval(input("Enter a Factorial number : "))
x4=1      
for i in range(1,x3):
    x4*=i
print("The factorial of the  ",x3, " is ", x4)
    
    