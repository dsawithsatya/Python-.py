# print "y" character using slice operator

x= "python"
print(x[1])
#print(x[-5])

# print "tho" character using slice 
y= "python"
print(y[2:5])

# print "yth" character using slice operator
z="python"
print(z[1:4])

# print "oht" character using slice operator
a="python"
print(a[4:1:-1])

# print "python" character using slice operator
b="python"
print(b)

# print y character using slice operator
c= "python"
# using slice operator
print(c[::-1])

# using join and reversed 
'''reverse="".join(reversed(c))
print(reverse)
'''

# using for loop
'''reverse=""
for i in range(len(c)):
    reverse=c[i]+reverse
print(reverse)
'''
# printing words 
new="Python full stack"
print(new[:6],new[12:17])

# printing "full" in reverse:

NEW="Python full stack"
print(NEW[10:6:-1])


print()
print()
# Using +ve and -Ve indexing print "full" String value:

print(NEW[7:11])
print(NEW[-10:-6])
# python in reverse using +ve and -ve
print()
print()
print(NEW[5::-1])
print(NEW[-12::-1])
# New string value in reverse:

print()
print()
print(NEW[::-1])
print(NEW[-1::-1])
# print only from one character to same other character : 
print()
print()
print(NEW[2:14])
print(NEW[-15:-3])
print()

# checking the string character is present or not:
if "g" in NEW:
    print("Hi")
else:
    print("bye")

#remove spaces without using split function:
print(NEW.replace(" ",""))

# print string value before 't' and after 't':
print(NEW.replace("thon full st",""))
