class BankAccount:
    no_of_cust=0
    acc_num=424110

    def __init__(self,name,mobile_no,initial_depo,pin):

        self.name             =name
        self.cust_acc_no      =BankAccount.acc_num
        self.mobile_no        =mobile_no
        self.acc_balance      =initial_depo
        self.pin              =pin

        BankAccount.acc_num    = BankAccount.acc_num + 1
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1


    def basic_details(self):
        print(f'user:{self.name}\t Account Number : {self.cust_acc_no}\t Account Balance : {self.acc_balance}')


    def deposit(self):
        amount=int(input("Enter the deposit amount :"))
        if amount > 0:
            self.acc_balance     = self.acc_balance + amount
            print(f"Transation completed. Current Balance : {self.acc_balance}")
        else:
            print("Invalid amount transation aborted")

    def withdrawl(self):
        amount=int(input("Enter the withdraw amount :"))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance   =self.acc_balance - amount
            print(f"Transation completed. current Balance : {self.acc_balance}")
        else:
            print("Invalid amount transation aborted")

    def payment(self,other):
        amount=int(input("Enter the payment amount :"))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance   =self.acc_balance  -  amount
            other.acc_balance  =other.acc_balance + amount
            print(f"Transation completed. current Balance : {self.acc_balance}")
        else:
            print("Invalid amount transation aborted")


if __name__=='__main__':

    cust1= BankAccount( name='Priyanshu Barapatre',mobile_no= 9371291928,initial_depo= 50000 , pin=2408)
    cust2= BankAccount( name='Sunil Barapatre'    ,mobile_no=8999156237 ,initial_depo= 100000, pin=1106)
    cust3= BankAccount( name='Suanda Barapatre'   ,mobile_no=9730618892 ,initial_depo= 40000 , pin=1234)
    cust4= BankAccount( name='Swayam Barapatre', mobile_no=9637760241   ,initial_depo= 10000 , pin=2005)
    
    
    print(cust1.basic_details())
    print(cust2.basic_details())
    print(cust3.basic_details())
    print(cust4.basic_details())

    cust1.deposit()
    print(cust1.basic_details())

    cust2.withdrawl()
    print(cust2.basic_details())

    cust1.payment(cust3)
    print(cust1.basic_details())
    print(cust3.basic_details())
