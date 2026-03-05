# PRACTICE CODE 

class student :
    subject = "Python"
    collage  = "BTIRT"
    Age = 22


stu1 = student()
stu2 = student()

print(stu1.collage,stu1.subject)

class student :
    def __init__ (self,name):
        self.name = name


stu1 = student("Amar")
print(stu1.name)

# instance Methods


class laptop:
    storage_type = "SSD"

    def __init__(self,RAM,storage):
        self.storage = storage
        self.RAM = RAM

    def get_info(self):
        print(f"Laptop has {self.RAM} Ram and {self.storage} storage")

l1 = laptop("16GB","256GB")
print(l1.RAM,l1.storage)

l1.get_info
