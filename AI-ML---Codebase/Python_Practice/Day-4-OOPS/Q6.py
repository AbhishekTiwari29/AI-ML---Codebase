from abc import ABC , abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self,stipend):
        self.stipend = stipend

    def calculate_salary(self):
        print(f"Intern Salary : {self.stipend}")

class FullTimeEmployee(Employee):
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        total = self.salary + self.bonus
        print(f"FullTimeEmployee Salary : {total}")

class ContractEmployee(Employee):
    def __init__(self,hours,rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        total = self.hours * self.rate
        print(f"ContractEmployee Salary : {total} ")


i = Intern(5000)
f = FullTimeEmployee(20000,3000)
c = ContractEmployee(8,500)

i.calculate_salary()
f.calculate_salary()
c.calculate_salary()
