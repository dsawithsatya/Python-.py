# Using variable declaration Rules we are going to declare the variables (Valid use cases):

# Declare variable using Rule 1, A-Z, a-z,A-Z and a-z, A-Z and a-z and 0-9:
# 1. Declare variable with A-Z :

import time
ABC= 200
print("Value of the variable",ABC)
print("Address of the variable:", id(ABC))
print("Type of the variable:",type(ABC))
time.sleep(2)
print("End of the 1st variable declaration")
print("============================================")
print()


# 2. Declare variable with a-z :

sir= 100
print("Value of the variable",sir)
print("Address of the variable:", id(sir))
print("Type of the variable:",type(sir))
time.sleep(2)
print("End of the 2nd variable declaration")
print("============================================")
print()

# 3. combination of upper and lower case :

ABCsir= 50
print("Value of the variable",ABCsir)
print("Address of the variable:", id(ABCsir))
print("Type of the variable:",type(ABCsir))
time.sleep(2)
print("End of the 3rd variable declaration")
print("============================================")
print()

# 4. Combination of upper case, lower case, and nubers with underscore '_' :


ABC_123_abc= 300
print("Value of the variable",ABC_123_abc)
print("Address of the variable:", id(ABC_123_abc))
print("Type of the variable:",type(ABC_123_abc))
time.sleep(2)
print("End of the 4th variable declaration")
print("============================================")
print()


# Declare variable using Rule 2, identifier/variable shouldn't start with 0-9 :
# 5. Declare variable without starting from 0-9 :

Abc_123= 350
print("Value of the variable",Abc_123)
print("Address of the variable:", id(Abc_123))
print("Type of the variable:",type(Abc_123))
time.sleep(2)
print("End of the 5th variable declaration")
print("============================================")
print()

# 6. Declare variable without starting from 0-9 :

A12345=3
print("Value of the variable",A12345)
print("Address of the variable:", id(A12345))
print("Type of the variable:",type(A12345))
time.sleep(2)
print("End of the 6th variable declaration")
print("============================================")
print()

# 7. Declare variable without starting from 0-9 :

Abcd_12345= 125
print("Value of the variable",Abcd_12345)
print("Address of the variable:", id(Abcd_12345))
print("Type of the variable:",type(Abcd_12345))
time.sleep(2)
print("End of the 7th variable declaration")
print("============================================")
print()

# 8. Declare variable without starting from 0-9 :

A123_abc= 325
print("Value of the variable",A123_abc)
print("Address of the variable:", id(A123_abc))
print("Type of the variable:",type(A123_abc))
time.sleep(2)
print("End of the 8th variable declaration")
print("============================================")
print()

# Using Rule 3 : there is no length limit
# we can use any kind of variables without limit for variable declaration:

# 9. Declare Variables without limit start with uppercase:
 
A11234567890_abcdefghijklmnopqrstuvwxyz= 325
print("Value of the variable",A11234567890_abcdefghijklmnopqrstuvwxyz)
print("Address of the variable:", id(A11234567890_abcdefghijklmnopqrstuvwxyz))
print("Type of the variable:",type(A11234567890_abcdefghijklmnopqrstuvwxyz))
time.sleep(2)
print("End of the 9th variable declaration")
print("============================================")
print()

# 10. Declare variables without limit start with lowercase:

busireddysatyanarayan14320000= 145
print("Value of the variable",busireddysatyanarayan14320000)
print("Address of the variable:", id(busireddysatyanarayan14320000))
print("Type of the variable:",type(busireddysatyanarayan14320000))
time.sleep(2)
print("End of the 10th variable declaration")
print("============================================")
print()

# 11. Declare variables without limit start with '_':

_abcdefghijklmnopqrstuvwxyz= 65
print("Value of the variable",_abcdefghijklmnopqrstuvwxyz)
print("Address of the variable:", id(_abcdefghijklmnopqrstuvwxyz))
print("Type of the variable:",type(_abcdefghijklmnopqrstuvwxyz))
time.sleep(2)
print("End of the 11th variable declaration")
print("============================================")
print()

# 12. Declare variables without limit, with mix of 0-9,A-Z, and a-z seperated by '_':

ABCDEFGHI_abcdefghi_1234567890= 90
print("Value of the variable",ABCDEFGHI_abcdefghi_1234567890)
print("Address of the variable:", id(ABCDEFGHI_abcdefghi_1234567890))
print("Type of the variable:",type(ABCDEFGHI_abcdefghi_1234567890))
time.sleep(2)
print("End of the 12th variable declaration")
print("============================================")
print()

# Declare a variable using rule 4: variable are case sensitive and also case insensitive

# case sensitive - which variables adress is different is called case sensitive
# case in_sensitive - which variables having same address is called case in_sensitive

# 13.Declare variables using case sensitive rule :

A= 123
B= 456
print("Values of the variable A & B :",A,"  &  ", B )
print("Address of the variables A & B :", id(A),"  &  ", id(B))
print("Type of the variables A & B:",type(A),"  &  ", id(B))
time.sleep(2)
print("End of the 13th variable declaration")
print("============================================")
print()
 
# 14. Declare the variables using case sensitive rule:

C= 321
D= 623
print("Values of the variable A & B :",C,"  &  ", D )
print("Address of the variables A & B :", id(C),"  &  ", id(D))
print("Type of the variables A & B:",type(C),"  &  ", id(D))
time.sleep(2)
print("End of the 14th variable declaration")
print("============================================")
print()

# 15. Declare  the variables using case in_censitive rule:
 
E= 1000
F= 1000
print("Values of the variable A & B :",E,"  &  ", F )
print("Address of the variables A & B :", id(E),"  &  ", id(F))
print("Type of the variables A & B:",type(E),"  &  ", id(F))
time.sleep(2)
print("End of the 15th variable declaration")
print("============================================")
print()

# 16. Declare  the variables using case in_censitive rule:
 
G= 2000
H= 2000
print("Values of the variable A & B :",G,"  &  ", H )
print("Address of the variables A & B :", id(G),"  &  ", id(H))
print("Type of the variables A & B:",type(G),"  &  ", id(H))
time.sleep(2)
print("End of the 16th variable declaration")
print("============================================")
print()

# Declare the variable using the rule 5 : Variable shouldn't start with reserve key:

'''keywords : ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
'break', 'class',  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import','in', 'is', 'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise', 'return', 'try','while', 'with', 'yield'] 
'''

# 17. Declare the Variables that can't start with Keyword True :

true=22
print("Value of the variable",true)
print("Address of the variable:", id(true))
print("Type of the variable:",type(true))
time.sleep(2)
print("End of the 17th variable declaration")
print("============================================")
print()

# 18. Declare the variables that can't start with keyword False :

false=33
print("Value of the variable",false)
print("Address of the variable:", id(false))
print("Type of the variable:",type(false))
time.sleep(2)
print("End of the 18th variable declaration")
print("============================================")
print()

# 19. Declare the variables that can't start with keyword None :
 
none=44
print("Value of the variable",none)
print("Address of the variable:", id(none))
print("Type of the variable:",type(none))
time.sleep(2)
print("End of the 19th variable declaration")
print("============================================")
print()

# 20. Declare the variables that can't start with keyword for :

For=55
print("Value of the variable",For)
print("Address of the variable:", id(For))
print("Type of the variable:",type(For))
time.sleep(2)
print("End of the 20th variable declaration")
print("============================================")
print()


