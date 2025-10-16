# Using upper() string method we can change the string into uppercase :

x="Welcome to Python Full Stack "
print()
print("upper() string method can change the string into uppercase : ")
print()
print(x.upper())
print()
# Using lower() string method we can change the string into lowercase :
print()
print("lower() string method can change the string into lowercase :")
print()
print(x.lower())

# Swapcase() method can change the string characters from upper to lower and lower to upper:
print()
print("swapcase() string method can swap the string into uppercase <==> lower : ")
print()
print(x.swapcase())

# Title() method can change the first letter of the word into upper case:
print()
print("title() string method can change the string starting letter into uppercase : ")
print()
print(x.title())

#capitalize() method can chnage the 1st letter of the paragraph into upper case:

y="i am very fine    "
print()
print("capitalize() string method can change the 1st letter of a string into uppercase ")
print()
z=y.capitalize()
print(z)


#strip()-->rstrip(),lstrip() which can remove the spaces from right and left side from the given string
print()
print("strip() string method can remove the spaces from string : ")
print()
print(y.rstrip(),"Thank you")

#split()-->rsplit() which can split the string values from right side from the given string
print()
print("split() string method can seperate the words from the  string : ")
print()
print(z.split())

# Join() method is used to join different data types ==> list,tuple,set,etc..

S=['I','AM','GOOD']
join=' '.join(S)
print(join)
print()

# count() method is used to count the no. of characters :

print(join.count('A'))

