def factorial(n):
    if n==0:
        return 1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(10))

#square of the values
s=lambda a:a*a
print(s(10))

#power of the given values
s1=lambda a: a**a
print("The square of {} is equal to {}".format(10,s1(10)))

s2=lambda a,b : a if a>b else b
print(f'The highest number of {10} and {20} is equal to  {s2(10,20)}')

#get the values of even numbers from the list using the filter function

l=[2,3,5,6,7,8]
def iseven(x):
    if x%2==0:
        return 1
    else:
        return 0
l1=tuple(filter(iseven,l))
print(l1)

#multiply 2 list of elements using lambda
l=[1,2,3,4,5,6,7]
l2=[8,9,10,11,12,13]
l1=map(lambda x,y:x*y,l,l2)
print(list(l1))
        
