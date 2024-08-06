class BalanceException(BaseException):
    def __init__(self,balance):
        self.balance = balance
class Account:
    def __init__(self,name,type,balance):
        self.name=name
        self.type=type
        self.balance=balance
    
    def withdrawAmount(self,wamt):
        if wamt>self.balance:
            raise BalanceException("Balance low")
        else:
            self.balance = self.balance-wamt
            print(f"Withdrawn, your available balance is {self.balance}")
    
    def depositAmount(self,dep):
        if dep<=0:
            raise BalanceException("Deposit low")
        else:
            self.balance = self.balance+dep
            print(f"Deposited, your available balance is {self.balance}")
    
    def checkBalance(self):
        if self.balance<=0:
            raise BalanceException("0 balance")
        else:
            print(self.balance)

a = Account("Vivek","Savings",2300)
a.checkBalance()
a.depositAmount(10)
a.withdrawAmount(24)
        