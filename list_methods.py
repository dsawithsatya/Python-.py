#list methods to be perform using the inbuilt methods:

#let us see with the methods and exampples of a methods 
#1. append() method it can be add the values to the list:
# inside method we can use only items for example - 1,2,"satya",..etc..
l1=[1,2,3,4,5]
print()
l1.append(1)
print()
print("The list after the append() method :",l1) 
print()
#2. extend() method to add the elements from list to other list:
#inside of the method we can use only iterables for example - l1,l2,or any variable names 
l2=[2,4,5,6]
l1.extend(l2)
print("The list after perform the extend() method :",l1)
print()
#3. insert() method to insert the values using the index :
# inside the method we can use (index values, item) for example -insert(0,10),(0,"satya"),..etc...
l1.insert(1,200)
print("The list after perform the insert() method :",l1)
print()

#4. remove() method to remove the values from a list :
#inside the method we can use only items for example - 1,2,"satya",..etc..
#note: we can remove the single item at a time using remove() method 
l1.remove(3)
l2.remove(4)
print("The list after remove the items in a list :",l1)
print()
print("The list after remove the items in a list :",l2)
print()

#5.pop() method can use to pop/remove the values using the indexing :
#without giving any items it can pop/remove the last ietm of the list:
# inside the method we can use only index values:
# let us see how we can pop/ remove without any item passing inside 

l1.pop()
print("After pop the values using the pop() method :",l1)
print()
l2.pop(1)
print("After pop the values using pop() with indedx",l2)
print()

# 6.index() method can be used to find the index of a item which you're passing :
# inside of a index method we can use only item for examples - 1,2,"satya",..etc.. 
l1.index(4)
print("Afetr getting the index of a value using index() method :", l1)
print()
l2.index(6)
print("After using index() method we have the list : ",l2)
print()

# 7.count() method can be used to count the values of a list :
# inside we can use only items, also we have to assign the output of a count to a variable:
l3=[2,3,4,2,3,5,3]
l4=l3.count(3)
print("Count the values given above using count() method :",l4)
print()

# 8.sort() method can be used to sort the values into ascending order:
# sort is used for the list, we can't use for other data types:
l3.sort()
print("after sort the values using sort() method the list will be :",l3)
print()
# if you want to print the values into descending order means, inside we can use "reverse=True"
l3.sort(reverse=True)
print("print the values after sort in descending order :",l3)
print()

#9.reverse() can be used to reverse the list
l4=["satya",1,3,"siva"]
l4.reverse()
print("reverse of a list after using reverse() method ",l4)
print()

#10.copy() is used to copy the items into a another variable also we have two two methods deepcopy and shallow copy:
l5=l4.copy()
print("Print the values after copy the items using copy() method form other list",l5)
print()

#11.sorted() is used to sort the values of any datatype:
l6=[0,1,2,-3,-4,-6]
l=sorted(l6)
print("after sorted a list will be :",l) 
print()
print("Afetr sorted",sorted(l6))
print()

#12.clear() method is used to clear the list of elements :
l6.clear()
print("After clear the values let us check is there any variable to carry items :",l6)
print()



















































