a="satya"
b='narayana'
print(''.join(a+b))

l=[1,2,3,4]
print(l.append(5))
l.extend([5,7])
print(l)

nums = [10, 20, 30, 40]

print(len(nums))         # 4
print()
print(max(nums))         # 40
print()
print(min(nums))         # 10
print()
print(sum(nums))         # 100
print()
print(sorted(nums))      # [10, 20, 30, 40]
print()

# Which methods can give None using inside the print() function 
print("Which methods can give None using inside the print() function")
print("================================================================")

print(nums.append(50))   # None  (but nums becomes [10,20,30,40,50])
print()
print(nums.extend([60])) # None  (nums = [10,20,30,40,50,60])
print()
print(nums.insert(1, 15))# None  (nums = [10,15,20,30,40,50,60])
print()
print(nums.remove(20))   # None  (nums = [10,15,30,40,50,60])
print()
print(nums.sort())       # None  (nums sorted = [10,15,30,40,50,60])
print()
print(nums.reverse())    # None  (nums reversed = [60,50,40,30,15,10])
print()

print(nums.pop())        # 10    (removed last element)
print()
print(nums.clear())      # None  (nums = [])
print()
print(nums.copy())       # []    (copy of empty list)
print()
print(nums.count(30))    # 0
print()
print(nums.append(40)) # For further usage I'm just append the values.
print()
print(nums.index(40))    # ValueError: 40 is not in list (because list is empty now)
print()

# To print the forward and Backward using while loop :
a1=input("Enter string : ")
s=0
j=len(a1)-1
while len(a1)>s:
    print(a1[s])
    s=s+1

print()   
while j>=0:
    print(a1[j])
    j=j-1
print()

i=-1
while i>=-len(a1):
    print(a1[i])
    i=i-1