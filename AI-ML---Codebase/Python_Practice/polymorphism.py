class Employee:
    def get_designation(self):
        print("Employee = Designation")

class Teacher(Employee):
    def get_designation(self):
        print("teacher = Designation")

t1 = Teacher()
t1.get_designation()    