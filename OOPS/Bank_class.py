class Bank:
    bal=500
    def accoutcreation(self,name,age,phnno,accountno):
        self.n=name
        self.a=age
        self.p=phnno

        self.a=accountno
    def deposit(self,amount):
        Bank.bal=Bank.bal+amount
        print("your account has been credited with ",Bank.bal)

    def customerdetails(self):
        print("customer name is",self.n)
        print("customer age is", self.a)
        print("customer number is", self.p)
        print("account number is", self.a)
        print("bank blance is", Bank.bal)
    def withdrawl(self,amnt):
        self.amnt=amnt
        if self.amnt>Bank.bal:
            print("insufficient balance")
        else:
            Bank.bal-=self.amnt
            print("your account has been credited with",self.amnt,"your available balane is",Bank.bal)

cust=Bank()
cust.accoutcreation("malu",18,9999999999,12345345)
am=int(input("give the amount you want to deposit"))
cust.deposit(am)
cust.customerdetails()
a=int(input("give the amount you want to withdraw"))
cust.withdrawl(a)
