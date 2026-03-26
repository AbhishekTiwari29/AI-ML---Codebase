class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        print("Managing Team")

class Developer(Employee):
    def work(self):
        print("Write a Code")

e1 = Manager("Abhishek",20000)
e1.work()