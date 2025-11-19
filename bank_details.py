class bank:
    a=0
    @staticmethod
    def balance():
        print("Your balance is : ",bank.a)
    @staticmethod
    def deposit():
        x=int(input(" Enter the deposit amount : "))
        bank.a+=x
        print("afetr deposit your balance is : ",bank.a)
    @staticmethod
    def withdraw():
        x=int(input("Enter withdraw amount : "))
        if x<bank.a and x%100==0:
            print("Withdraw suucessfull..")
        else:
            print("Enter correct amount ")
        bank.a-=x
        print("After withdrawal your balance is : ",bank.a)
t=bank()
while True:
    print("Select your Bank Details .... ")
    print()
    print("========================================")
    print()
    print("1.Balance\n","2.Deposit\n","3.withdraw")
    print()
    print("=========================================")
    e=int(input("select your query.... "))
    if e==1:
        t.balance()
    elif e==2:
        t.deposit()
    elif e==3:
        t.withdraw()
    else:
        print("Please select from the above options..\n")
        break
    print("Do u have any query.....yes/no \n")
    x2=input("Enetr your answer..\n")
    if x2=="yes":
        pass
    else:
        break

        
    