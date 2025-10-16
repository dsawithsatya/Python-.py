# Do the operations using the input() function from the user:
# print the single value from the keyboard:
import time
print()
a=input("enter the value of a :")
print()
print(type(a))
print ()
time.sleep(1)
print ("end of the input() function ")
print()
 
# Do the arthimetic operations using input function:
# using two variables perform the operations:
a1=input("Enter a value for a1 :")  # assume a1=10
a2=input("Enter a value for a2 :")    # assume a2=20
print()
print(a1+a2) #output should be 1020
print()
time.sleep(1)
print("end of the input function using two variables :")
print()

# From the above code we understand that whatever we enter from the keyboard it is consider as string character.so, to overcome this we have to use typecasting:
#using type casting we can get the type of the characters it may be int, float, bool, or complex
# Let us see with an examples we can understand how the arthmetic operations done based on typecasting:
#let us start with the int() typecasting
b1=int(input("Enter the b1 value :"))
print()
b2=int(input("Enter the b2 value :"))
print()
print("Type of the b1 value :",type(b1),"\n Type of the b2 value :",type(b2))
print()
print("Add the b1 and b2 value :",b1+b2)
print()
print("multiply the b1 and b2 value :",b1*b2)
print()
print("subtract the b1 and b2 value :",b1-b2)
print()
print("Division of the b1 and b2 value :",b1/b2)
print()
print("Module of the b1 and b2 value :",b1%b2)
print()
time.sleep(1)
print("End of the int() typecasting ")
print()

# Then move to the next typecasting float()

c1=float(input("Enter the c1 value :"))
print()
c2=float(input("Enter the c2 value :"))
print()
print("Type of the c1 value :",type(c1),"\n Type of the c2 value :",type(c2))
print()
print("Add the c1 and c2 value :",c1+c2)
print()
print("multiply the c1 and c2 value :",c1*c2)
print()
print("subtract the c1 and c2 value :",c1-c2)
print()
print("Division of the c1 and c2 value :",c1/c2)
print()
print("Module of the c1 and c2 value :",c1%c2)
print()
time.sleep(1)
print("End of the float() typecasting ")
print()

#then move to the next type casting bool()

d1=bool(input("Enter the d1 value :"))
print()
d2=bool(input("Enter the d2 value :"))
print()
print("Type of the d1 value :",type(d1),"\n Type of the d2 value :",type(d2))
print()
print("Add the d1 and d2 value :",d1+d2)
print()
print("multiply the d1 and d2 value :",d1*d2)
print()
print("subtract the d1 and d2 value :",d1-d2)
print()
print("Division of the d1 and d2 value :",d1/d2)
print()
print("Module of the d1 and d2 value :",d1%d2)
print()
time.sleep(1)
print("End of the bool() typecasting ")
print()

#Let us move to eval() function which is used for every datatype whatever we enter from the keyboard:
#eval() function can perform set of operations as follows :
#1. NAO - normal arthmetic operations :
e1=eval(input("Enter the e1 value for the NAO : "))
print()
e2=eval(input("Enter the e2 value for the NAO :"))
print()
print("Datatype of the e1 :",type(e1),"\n Datatype of the e2 :",type(e2))
print()
print("===== operations to be perform using e1 and e2 values ======")
print()
print("Add the e1 and e2 value :",e1+e2)
print()
print("multiply the e1 and e2 value :",e1*e2) # its doesn't work for the string  values # but one str() and one int() can execute
print()
print("subtract the e1 and e2 value :",e1-e2) # its doesnt work for any string or str()and int()
print()
print("Division of the e1 and e2 value :",e1/e2) # its doesnt work for any string or str()and int()
print()
print("Module of the e1 and e2 value :",e1%e2) # its doesnt work for any string or str()and int()
print()
time.sleep(1)
print("End of the eval() typecasting function ")
print()

# 2. string concatination using two strings:

s1=eval(input("Enter a s1 string characters for SC :"))
print()
s2=eval(input("Enter the s2 string characters for SC:"))
print()
print("Datatype of s1 is :",type(s1),"\n Datatype of s2 is :",type(s2))
print
print("Print the string concatination using '+' operator :",s1+s2)
print()
time.sleep(1)
print(" End of the string concatination ")
print()

#print the string repetation values from the given string 
str1=eval(input("Enter a str1 string characters for SR :"))
print()
str2=eval(input("Enter the str2  characters for SR:"))
print()
print("Datatype of s1 is :",type(str1),"\n Datatype of s2 is :",type(str2))
print
print("Print the string concatination using '*' operator :",str1*str2)
print()
time.sleep(1)
print(" End of the string repetation ")
print()

# Write a python script using eval function perform the above 3 types but using a single variable:
#1. write the code to perform the NOA using single variable
eva=eval(input("Enter the value for NAO :"))
print()
print("Datatype of the eval :",type(eva))
print()
print("print the NAO value using the one variable :",eva)
time.sleep(1)
print()
print("End of the NAO using the single variable")
print()

#2. Write thr code to perform the SC using single variable

eval1=eval(input("Enter the value for SC :"))
print()
print("datatype of the eval1 variable :",type(eval1))
print()
print("Print the SC characters using single variable :",eval1)
print()
time.sleep(1)
print("End of the SC using the single variable ")
print()

#3. write the code to perform the SR using the single variable

eval2=eval(input("Enter the value for the SR : "))
print()
print("datatype of the eval1 variable :",type(eval2))
print()
print("Print the SR characters using single variable :",eval2)
print()
time.sleep(1)
print("End of the SR using the single variable ")
print()

 

