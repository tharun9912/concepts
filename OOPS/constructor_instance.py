class BankAccount:
    def __init__(self,Account_Holder,Balance):
        self.Account_Holder= Account_Holder
        self.Balance = Balance

    def deposit(self,amount):
        self.Balance+=amount
        self.check_balance()

    def withdraw(self,amount):
        self.Balance-=amount
        self.check_balance()

    def check_balance(self):
        print(f"Balance :{self.Balance}") 
    
if __name__=="__main__":

    account1 = BankAccount("Tharun",2000)
    account1.deposit(500)
    account1.withdraw(2000)
