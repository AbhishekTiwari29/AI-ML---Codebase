class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,amount): 
        self.balance = self.balance + amount
        print("Amount deposited Successfully")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawal Successfully")

    def check_balance(self):
        print(self.balance)

acc1 = BankAccount(45784515,"Abhishek",4000)
print(acc1.account_number,acc1.owner_name,acc1.balance)
acc1.deposit(2000)
print(acc1.balance)
acc1.withdraw(1000)
print(acc1.balance)
acc1.check_balance()