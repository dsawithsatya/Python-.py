# from collections import Counter
# d=[1,2,3,4,1,4,1,3,6]
# print(dict(Counter(d)))

d=[1,2,3,1,4,5,1,2,3]
d1={}
for i in d:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1)