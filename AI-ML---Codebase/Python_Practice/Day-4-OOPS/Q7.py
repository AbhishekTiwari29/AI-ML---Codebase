class Person:
    def __init__(self,name,age=None,address=None):
        self.name = name
        self.age = age
        self.address = address

    def show(self):
        print(self.name,self.age,self.address)

p1 = Person("Abhishek")
p2 = Person("Abhishek",21)
p3 = Person("Abhishek",21,"Subash Nagar")

p1.show()
p2.show()
p3.show()