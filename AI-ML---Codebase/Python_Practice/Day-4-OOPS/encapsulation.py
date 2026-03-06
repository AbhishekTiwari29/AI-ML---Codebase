class bankAccount:
    def __init__(self,name,balance):
        self.name = name  #public
        self.__balance = balance   #private


    def get_balance(self):   #getter 
        return self.__balance
    
    def set_balance(self,newBalance):   #setter
        self.__balance = newBalance

acc1 = bankAccount("Abhishek",100000)
acc2 = bankAccount("Rohit",300000)
acc1.set_balance(200000)
print(acc1.name,acc1.get_balance())
print(acc2.name,acc2._bankAccount__balance)

