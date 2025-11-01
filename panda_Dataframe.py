import pandas as pd
# #create a dataframe using for loop to add the elements
# x1=[]
# y=int(input("Enter no.of entries should be added : "))
# for i in range(y):
#     name=input("Enter name : ")
#     roll_no=int(input("Enter roll_no"))
#     sec=input("Enter sec: ")
#     x1.append([name,roll_no,sec])
# print()
# x=pd.DataFrame(x1,columns=["name","roll_no","Sec"])
# print(x)

#usnig dictonary add the two dictonaries and get the dataframes:
x2={"name":["satya","siva"],"roll_no":[1,2],"sec":["A","B"]}
x3={"name":["siva","satya"],"roll_no":[80,90],"sec":[80,90]}
df1=pd.DataFrame(x2)
df2=pd.DataFrame(x3)
df=pd.concat([df1,df2],ignore_index=True)
print(df)
print()

print(df.fillna(0))
print()
print(df.head(2))
print()
print(df.tail(2))
print()
print(df.duplicated())
print()
print(df.isnull())
print()

x=2911
x1=[""]
while 0<x:
    z=x%10
    x//=10
    x1.insert(1,str(z))
print("0".join(x1))

