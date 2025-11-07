x=[{"Pname":"apple","pprice":200,"pquantity":100}]


def views():
# view the keys and values inside the dictonary in list:
    for i in x:
        for i,j in i.items():
            print(i,j)
# append the new items at the last of the list:
def add():
    x1=int(input("Enter how many entries to be adding : "))
    for i in range(x1):
        a=input("Enter a pname : ")
        b=input("Enter the pprice :")
        c=input("enter pquantity : ")
        x.append({'pname':a,'pprice':b,'pquantity':c})
    print(x)

#we can update the data using update() method as well as single value update also:

def update():
    for i in x[0]:
        print(i)
            
            
    
while True:
    print('-------------------------------------------')
    print('1.view\n2.add\n3.update\n4.delete')
    print('-------------------------------------------')
    choice=int(input("Enter ur choice"))
    if choice==1:
        views()
    elif choice==2:
        add()
    else:
        break


