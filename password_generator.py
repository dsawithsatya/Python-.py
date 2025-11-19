import random
lower="abcdefghijklmnopqrstuvwxyz"
upper=lower.upper()
numbers="0123456789"
symbols="!@#$%^&*()_-+=?<>"
keys=lower+upper+numbers+symbols
length=int(input("Enter length of the password : "))

password="".join(random.sample(keys,length))
print("The genarated password will be : ",password)