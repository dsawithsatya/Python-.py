x="a3bb2c2"
s=""
y=[]
for i in x:
    if i.isdigit():
        s=s+"/"
        y.append(int(i))
    else:
        s=s+i
z=s.split("/")
for i,j in zip(z,y):
    print(i*j)
    